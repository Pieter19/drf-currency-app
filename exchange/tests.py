import os

import vcr
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from exchange.models import Currency, CurrencyRate

my_vcr = vcr.VCR(
    cassette_library_dir=os.path.dirname(os.path.realpath(__file__)),
    record_mode='once'
)


class CurrencyRateUpdateCurrencyTestCase(APITestCase):
    url = reverse('currencyrate-update-currency')

    @my_vcr.use_cassette('fixtures/rss_currencies.yaml')
    def test_updating_currencies(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, Currency.objects.count())
        self.assertEqual(3, CurrencyRate.objects.count())


class CurrencyRateTestCase(APITestCase):
    url = reverse('currencyrate-list')

    def setUp(self):
        self.currency_name = 'PLN'
        self.date = '2019-01-30T14:15:00+01:00'
        self.exchange_rate = '21.37'
        currency_obj = Currency.objects.create(name=self.currency_name)
        CurrencyRate.objects.create(currency=currency_obj, date=self.date, exchange_rate=self.exchange_rate)

    def test_list_currency_rates(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        resp_json = response.data
        self.assertEqual(self.currency_name, resp_json[0]['currency']['name'])
        self.assertEqual(float(self.exchange_rate), resp_json[0]['exchange_rate'])
