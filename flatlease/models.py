from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.contrib.auth.models import User, Group

health_type_dict = (
    ('healthy', 'Здоров'),
    ('sick', 'Болен'),
    ('addict', 'Наркодиспансер'),
    ('psycho', 'Психодиспансер'),
)
pay_type_dict = (
    ('cash', 'Наличные'),
    ('transfer', 'Перевод'),
    ('card', 'Банковская карта'),
    ('inside', 'Внутренний перевод'),
)
doc_type_dict = (
    ('application', 'Заявление'),
    ('form', 'Анкета'),
    ('contract', 'Договор'),
)


def photo_file_path(instance, filename):
    return 'client_media/{0}_{1}/{2}'.format(instance.id, instance.last_name, filename)


def content_file_path(instance, filename):
    return 'client_media/{0}_{1}/{2}'.format(instance.owner.id, instance.owner.last_name, filename)


def managers():
    return {'groups': Group.objects.get(name='Manager')}

class Person(models.Model):
    pub_date = models.DateTimeField("Время добавления", auto_now_add=True)
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    second_name = models.CharField("Отчество", max_length=30, blank=True)
    birthday = models.DateField("День рождения", blank=True)
    phone = models.CharField("Телефон", max_length=12)
    residence = models.CharField("Адрес проживания", max_length=100)

    class Meta:
        abstract = True

    def age(self):
        return round((date.today() - self.birthday).days/365)

    def is_adult(self):
        return self.age() >= 18


class Client(Person):
    manager = models.ForeignKey(User, limit_choices_to=managers, verbose_name="Менеджер")
    birthplace = models.CharField("Место рождения", max_length=100)
    registration = models.CharField("Регистрация по месту жительства", max_length=100)
    email = models.EmailField("EMail", blank=True)
    health = models.CharField("Состояние здоровья", max_length=20, choices=health_type_dict, default=health_type_dict[0][0])
    workplace = models.CharField("Место работы", max_length=50, blank=True)
    work_position = models.CharField("Должность", max_length=50, blank=True)
    salary = models.DecimalField("Заработная плата", max_digits=10, decimal_places=2)
    profit = models.DecimalField("Дополнительный доход", max_digits=10, decimal_places=2, blank=True)
    photo = models.ImageField("Фотография", upload_to=photo_file_path, blank=True)
    monthly_payment = models.DecimalField("Ежемесячный платеж", max_digits=10, decimal_places=2, editable=False, default=0)
    comment = models.TextField("Дополнительный комментарий", max_length=500, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def balance(self):
        """Возвращает сумму всех транзакций обьекта"""
        return sum((transaction.count for transaction in self.transaction_set.all()))
    balance.short_description = 'Баланс'

    def future(self):
        """Определяет потецнциальный клиент или нет, проверяя наличие у него договора"""
        return (not self.document_set.filter(type='contract'))
    #Доделать условие
    def debt(self):
        try:
            return self.monthly_payment > self.transaction_set.latest('pub_date').count
        except ObjectDoesNotExist:
            return None
    debt.short_description = 'Долг'

    def __str__(self):
        return " ".join([self.last_name, self.name, self.second_name])


class FixedProperty(models.Model):
    location = models.CharField("Местоположение", max_length=50, unique=True)
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2, default=0)
    owner = models.ForeignKey(Client, verbose_name="Клиент")

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"

    def __str__(self):
        return self.location


class Transaction(models.Model):
    owner = models.ForeignKey(Client, verbose_name="Клиент")
    count = models.DecimalField("Платеж", max_digits=10, decimal_places=2, default=0)
    type = models.CharField("Тип платежа", max_length=20, choices=pay_type_dict, default=pay_type_dict[0][0])
    pub_date = models.DateTimeField("Дата платежа", auto_now_add=True)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return " ".join([str(self.count), self.type, str(self.pub_date)])


class Document(models.Model):
    owner = models.ForeignKey(Client, verbose_name="Клиент")
    type = models.CharField("Тип", max_length=20, choices=doc_type_dict, default=doc_type_dict[0][0])
    document = models.FileField("Документ", upload_to=content_file_path)
    pub_date = models.DateTimeField("Время добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.name


class Passport(models.Model):
    owner = models.OneToOneField(Client, verbose_name="Клиент", primary_key=True)
    number = models.IntegerField("Серия и Номер")
    data = models.DateField("Дата выдачи")
    whom = models.TextField("Кем выдан", max_length=100)
    image = models.ImageField("Паспорт", upload_to=content_file_path)

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"

    def __str__(self):
        return str(self.number)


class Relative(Person):
    owner = models.ForeignKey(Client, verbose_name="Клиент")

    class Meta:
        verbose_name = "Родственник"
        verbose_name_plural = "Родственники"

    def __str__(self):
        return " ".join([self.last_name, self.name, self.second_name])


class Spouse(Person):
    owner = models.OneToOneField(Client, verbose_name="Клиент")
    workplace = models.CharField("Место работы", max_length=50, blank=True)
    work_position = models.CharField("Должность", max_length=50, blank=True)
    salary = models.DecimalField("Заработная плата", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Супруг(а)"
        verbose_name_plural = "Супруги"

    def __str__(self):
        return " ".join([self.last_name, self.name, self.second_name])