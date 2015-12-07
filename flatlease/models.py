from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django.contrib.auth.models import User, Group
from base.models import Client
from django.utils import timezone


# def photo_file_path(instance, filename):
#     return 'client_media/{0}/{1}'.format(instance.id, filename)
#
#
# def content_file_path(instance, filename):
#     return 'client_media/{0}/{1}'.format(instance.owner.id, filename)


class FixedProperty(models.Model):
    owner = models.ForeignKey(Client, verbose_name="Клиент")
    location = models.CharField("Местоположение", max_length=50, unique=True)
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2, default=0)
    number = models.CharField("Кадастровый номер", max_length=50, blank=True)
    build_year = models.DateField("Дата постройки")

    class Meta:
        verbose_name = "Недвижимость"
        verbose_name_plural = "Недвижимость"

    def __str__(self):
        return self.location
