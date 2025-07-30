from django.db import models
from django.contrib.auth.models import AbstractUser

class Organisation(models.Model):
    name = models.CharField(verbose_name='Наименование')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class CustomUser(AbstractUser):
    father_name = models.CharField(verbose_name='Отчество')
    organisation = models.ForeignKey(Organisation, verbose_name='Организация', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Author(models.Model):
    id = models.UUIDField(verbose_name='ID', primary_key=True)
    first_name = models.CharField(verbose_name='Имя')
    last_name = models.CharField(verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    id = models.UUIDField(verbose_name='ID', primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название')
    pages = models.PositiveIntegerField(verbose_name='Количество страниц')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'