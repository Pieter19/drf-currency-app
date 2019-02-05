# Simple DRF Currency Rates App

### Installation

Install dependencies:
```
$ pip install -r requirements.txt
``` 

Setup database or use the sqlite one:

```
$ django-admin migrate
```

Run the app as you normally would:

```
$ python manage.py runserver
```

Testing the app:


```
$ pip install -r requirements_tests.txt
$ python manage.py test
```

### About the app

App uses `django` with `djangorestframework` and utilizes `ViewSet`s as a main way to view data.

### Endpoints

`/currencies/` - lists available currencies

`/currency_rates/` - lists currency rates, latest first

`/currency_rates/<currency_name>/` - lists currency rates for single currency, latest first

`/currency_rates/update_currency/` - updates currencies as well as currency rates with European Central Bank as source of data (additional currencies can be provided in `settings.py`)

### Improvements to be made
* Move `RSS_CURRENCIES` links to `Currency` model
* More tests
* Use `Factory Boy` in tests