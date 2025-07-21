from django.db import models

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