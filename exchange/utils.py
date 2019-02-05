import feedparser

from currency.settings import RSS_CURRENCIES
from exchange.models import CurrencyRate, Currency


def update_currency():
    for url in RSS_CURRENCIES:
        response = feedparser.parse(url)
        entry = response['entries'][0]
        currency_obj, _ = Currency.objects.get_or_create(name=entry['cb_targetcurrency'])
        CurrencyRate.objects.get_or_create(
            currency=currency_obj,
            date=entry['updated'],
            defaults={'exchange_rate': entry['cb_exchangerate'].split('\n', 1)[0]}
        )
