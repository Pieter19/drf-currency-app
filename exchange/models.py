from django.db import models


class CurrencyRate(models.Model):
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    date = models.DateTimeField()
    exchange_rate = models.FloatField()

    class Meta:
        ordering = ['-date']


class Currency(models.Model):
    name = models.CharField(max_length=20)
