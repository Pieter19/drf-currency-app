from django.urls import path, include
from rest_framework.routers import DefaultRouter

from exchange.views import CurrencyViewSet, CurrencyRateViewSet

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'currency_rates', CurrencyRateViewSet)
router.register(r'currency_rates/(?P<currency_name>[a-zA-Z0-9]+)', CurrencyRateViewSet)

urlpatterns = [
    path('', include(router.urls))
]
