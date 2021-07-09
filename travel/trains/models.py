from django.db import models
from django.core.exceptions import ValidationError
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Номер поїзда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Час путі')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='from_city_set', verbose_name='З міста')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='to_city_set', verbose_name='У місто')

    def __str__(self):
        return f'Поїзд №{self.name} з міста {self.from_city} у місто {self.to_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Зменить місто прибуття')
        qs = Train.objects.filter(from_city=self.from_city,
                                  to_city=self.to_city,
                                  travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Зменить час подорожжі')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Поїзд'
        verbose_name_plural = 'Поїзда'
        ordering = ['travel_time']
