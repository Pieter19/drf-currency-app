from rest_framework import serializers

from exchange.models import CurrencyRate, Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('name',)


class CurrencyRateSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = CurrencyRate
        fields = ('currency', 'date', 'exchange_rate')
