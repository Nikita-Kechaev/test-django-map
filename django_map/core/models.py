from django.contrib.gis.db import models
from django.db.models import UniqueConstraint


class City(models.Model):
    name = models.CharField(
        blank=False,
        max_length=100,
        verbose_name='Название города')
    location = models.PointField(
        verbose_name='Географическое расположение(широта/долгота)'
    )

    class Meta:
        verbose_name = 'город России'
        verbose_name_plural = 'города России'
        constraints = [
            UniqueConstraint(
                fields=['name', 'location'], name='unique city')
        ]
