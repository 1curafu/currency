from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'Dollar'
    CHF = 3, 'Swiss Franc'
    GBP = 4, 'Pound sterling'
