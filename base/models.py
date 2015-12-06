from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.contrib.auth.models import User, Group
from django.utils import timezone

health_type_dict = (
    ('Здоров', 'Здоров'),
    ('Серьезные проблемы со здоровьем', 'Серьезные проблемы со здоровьем'),
    ('На учете в наркодиспансере', 'На учете в наркодиспансере'),
    ('На учете в психдиспансере', 'На учете в психдиспансере'),
)
pay_type_dict = (
    ('Наличные', 'Наличные'),
    ('Безналичный', 'Безналичный'),
    ('Внутренний', 'Внутренний перевод'),
)
doc_type_dict = (
    ('Заявление', 'Заявление'),
    ('Анкета', 'Анкета'),
    ('Договор', 'Договор'),
)
relation_type_dict = (
    ('Отец', 'Отец'),
    ('Мать', 'Мать'),
    ('Ребенок', 'Ребенок'),
)


def photo_file_path(instance, filename):
    return 'client_media/{0}/{1}'.format(instance.id, filename)


def content_file_path(instance, filename):
    return 'client_media/{0}/{1}'.format(instance.owner.id, filename)


def managers():
    try:
        return {'groups': Group.objects.get(name='managers')}
    except ObjectDoesNotExist:
        return {'is_stuff': True}


class Person(models.Model):
    pub_date = models.DateTimeField("Время добавления", auto_now_add=True)
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    second_name = models.CharField("Отчество", max_length=30, blank=True)
    birthday = models.DateField("День рождения")
    phone = models.CharField("Телефон", max_length=12, blank=True)
    residence = models.CharField("Адрес проживания", max_length=100, blank=True)

    class Meta:
        abstract = True

    def age(self):
        return round((date.today() - self.birthday).days/365)

    def is_adult(self):
        return self.age() >= 18


class Client(Person):
    manager = models.ForeignKey(User, limit_choices_to=managers, verbose_name="Менеджер")
    email = models.EmailField("EMail", blank=True)
    health = models.CharField("Состояние здоровья", max_length=50, choices=health_type_dict, default=health_type_dict[0][0])
    workplace = models.CharField("Место работы", max_length=50, blank=True)
    work_position = models.CharField("Должность", max_length=50, blank=True)
    salary = models.DecimalField("Заработная плата", max_digits=10, decimal_places=2, default=0)
    profit = models.DecimalField("Дополнительный доход", max_digits=10, decimal_places=2, default=0)
    photo = models.ImageField("Фотография", upload_to=photo_file_path, default="/static/flatlease/images/userPlaceholder.png")
    monthly_payment = models.DecimalField("Ежемесячный платеж", max_digits=10, decimal_places=2, default=0)
    comment = models.TextField("Дополнительный комментарий", max_length=500, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def balance(self):
        """Возвращает сумму всех транзакций обьекта"""
        return sum((transaction.count for transaction in self.transaction_set.all()))
    balance.short_description = 'Баланс'

    def is_potential(self):
        """Определяет потецнциальный клиент или нет, проверяя наличие у него договора"""
        return not self.document_set.filter(type='contract').exists()
    #Доделать условие
    def debt(self):
        try:
            return self.monthly_payment > self.transaction_set.latest('pub_date').count
        except ObjectDoesNotExist:
            return True
    debt.short_description = 'Долг'

    def __str__(self):
        return " ".join([self.last_name, self.name, self.second_name])


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
    number = models.CharField("Серия и Номер", max_length=10)
    date = models.DateField("Дата выдачи")
    whom = models.TextField("Кем выдан", max_length=100)
    image = models.ImageField("Паспорт", upload_to=content_file_path)
    birthplace = models.CharField("Место рождения", max_length=100)
    registration = models.CharField("Регистрация по месту жительства", max_length=100)

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"

    def __str__(self):
        return str(self.number)


class Relative(Person):
    owner = models.ForeignKey(Client, verbose_name="Клиент")
    relation = models.CharField("Родство", choices=relation_type_dict, max_length=10, default=relation_type_dict[0][0])

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