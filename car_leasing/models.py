from django.db import models
from base.models import Client, Document, Transaction
from django.utils import timezone


def photo_file_path(instance, filename):
    return 'client_media/{0}/{1}'.format(instance.id, filename)


def content_file_path(instance, filename):
    return 'client_media/{0}/{1}'.format(instance.owner.id, filename)


class Brand(models.Model):
    name = models.CharField("Производитель", max_length=50)
    logo = models.ImageField("Лого", blank=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Model(models.Model):
    brand = models.ForeignKey(Brand, verbose_name="Производитель", blank=True)
    name = models.CharField("Модель", max_length=50)
    year = models.DateField("Год выпуска")

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class Car(models.Model):
    owner = models.ForeignKey(Client, verbose_name="Клиент", blank=True)
    model = models.ForeignKey(Model, verbose_name="Производитель", blank=True)
    color = models.CharField("Цвет", max_length=50, blank=True)
    man_date = models.DateField("Дата выпуска")
    mileage = models.IntegerField("Пробег", default=0)
    photo = models.ImageField("Фотография", upload_to=photo_file_path, blank=True)
    comment = models.TextField("Комментарий", max_length=500, blank=True)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


