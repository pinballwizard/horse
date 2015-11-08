from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Client(models.Model):
    pub_date = models.DateTimeField("Время добавления", auto_now_add=True)
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    second_name = models.CharField("Отчество", max_length=30, blank=True)
    birthday = models.DateField("День рождения")
    residence = models.CharField("Адрес проживания", max_length=50)
    phone = models.CharField("Телефон", max_length=15)
    email = models.EmailField("EMail", blank=True)
    client_media = 'client_media/%s_%s', (last_name, str(id))
    photo = models.ImageField("Фотография", upload_to=client_media, blank=True)
    passport = models.ImageField("Паспорт", upload_to=client_media, blank=True)
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
        if not self.document_set.filter(type='contract'):
            return False
        else:
            return True
#Доделать условие
    def debt(self):
        try:
            if self.monthly_payment > self.transaction_set.latest('pub_date').count:
                return True
            else:
                return False
        except ObjectDoesNotExist:
            return
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
    pay_type_dict = (
        ('cash', 'Наличные'),
        ('transfer', 'Перевод'),
        ('card', 'Банковская карта'),
        ('inside', 'Внутренний перевод'),
    )

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
    type_dict = (
        ('application', 'Заявление'),
        ('form', 'Анкета'),
        ('contract', 'Договор'),
    )

    owner = models.ForeignKey(Client, verbose_name="Клиент")
    type = models.CharField("Тип", max_length=20, choices=type_dict, default=type_dict[0][0])
    document = models.FileField("Документ", upload_to=owner)
    pub_date = models.DateTimeField("Время добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.name