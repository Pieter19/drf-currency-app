from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from exchange.models import CurrencyRate, Currency
from exchange.serializers import CurrencyRateSerializer, CurrencySerializer
from exchange.utils import update_currency


class CurrencyViewSet(ListModelMixin, GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyRateViewSet(ListModelMixin, GenericViewSet):
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    lookup_url_kwarg = 'currency'
    lookup_field = 'currency'

    @action(detail=False, methods=['get'])
    def update_currency(self, request):
        update_currency()
        return Response({'succeeded': True})

    def get_queryset(self):
        currency_name = self.kwargs.get('currency_name')
        if currency_name:
            return self.queryset.filter(currency__name=currency_name)
        else:
            return self.queryset
