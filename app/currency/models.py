from django.db import models

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD,
    )   # if field has choices get_{field_name}_display() - get_currency_display()
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=255)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.URLField(max_length=255)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=False, blank=False)
