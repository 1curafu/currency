from django.db import models

from currency.choices import RateCurrencyChoices
from django.templatetags.static import static


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD,
    )   # if field has choices get_{field_name}_display() - get_currency_display()
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('bank.jpeg')

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}'


class ContactUs(models.Model):
    name = models.CharField(max_length=128, default='')
    email_from = models.EmailField(max_length=255)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


def avatar_path(instance, filename):
    return f'banks/{instance.id}/{filename}'


class Source(models.Model):
    name = models.CharField(max_length=64)
    source_url = models.URLField(max_length=255)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=False, blank=False)
    avatar = models.FileField(
        default=None,
        null=True,
        blank=True,
        upload_to=avatar_path
    )

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('bank.jpeg')

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=255)
    time = models.FloatField()

    def __str__(self):
        return f'ID: {self.id}, Path: {self.path}, Method: {self.request_method}'
