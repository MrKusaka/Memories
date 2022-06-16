from django.db import models


class Memory(models.Model):
    place = models.CharField('Название места:', max_length=100)
    comments = models.TextField('Комментарий')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.place
