from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="Маршрут")
    travel_times = models.PositiveSmallIntegerField(verbose_name='Час путі')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_from_city_set', verbose_name='З міста')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='route_to_city_set', verbose_name='У місто')
    trains = models.ManyToManyField('trains.Train', verbose_name='Сиписок поїздів')

    def __str__(self):
        return f'Маршрут {self.name} з міста {self.from_city} у місто {self.to_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршрути'
        ordering = ['travel_times']

