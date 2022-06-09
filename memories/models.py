from django.db import models


class Task(models.Model):
    title = models.CharField('Название воспоминания', max_length=50)
    memory = models.TextField('Воспоминание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пупа'
        verbose_name_plural = 'Пупы'