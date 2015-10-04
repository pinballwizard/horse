from django.db import models


class Client(models.Model):
    name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    second_name = models.CharField("Отчество", max_length=30, blank=True)
    birthday = models.DateField("День рождения")
    residence = models.CharField("Адрес проживания", max_length=50)
    phone = models.CharField("Телефон", max_length=15)
    email = models.EmailField("EMail", blank=True)
    photo = models.ImageField("Фотография", upload_to='client_photo')
    passport = models.ImageField("Паспорт", upload_to='client_passport')
    deposit = models.DecimalField("Депозит", max_digits=10, decimal_places=2, default=0)
    comment = models.TextField("Дополнительный комментарий", max_length=500, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return " ".join([self.last_name, self.name, self.second_name])


class FixedProperty(models.Model):
    location = models.CharField("Местоположение", max_length=50, unique=True)
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2, default=0)
    owner = models.ForeignKey(Client)

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"

    def __str__(self):
        return self.location
