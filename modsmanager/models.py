from django.db import models

class Mod(models.Model):
    name = models.CharField('Название', max_length=200)
    size = models.IntegerField('Размер')
    photo = models.URLField('Иконка мода')
    genre = models.CharField('Жанр', max_length=200)
    notforchildren = models.BooleanField('Запрещено для детей', default=False)
    link = models.URLField('Ссылка')
    def __str__(self):
        return f'Модификация: {self.name}'
    class Meta:
        verbose_name = 'Мод'
        verbose_name_plural = 'Моды'

class Perevod(models.Model):
    name = models.CharField('Название', max_length=200)
    size = models.IntegerField('Размер')
    photo = models.URLField('Иконка перевода')
    genre = models.CharField('Жанр', max_length=200)
    notforchildren = models.BooleanField('Запрещено для детей', default=False)
    link = models.URLField('Ссылка')
    def __str__(self):
        return f'Перевод: {self.name}'
    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'