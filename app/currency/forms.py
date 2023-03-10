from django import forms

from currency.models import Rate, ContactUs, Source, RequestResponseLog


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency',
            'buy',
            'sell',
            'source'
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email_from',
            'subject',
            'message'
        )


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
            'country',
            'city'
        )


class RequestResponseLogForm(forms.ModelForm):
    class Meta:
        model = RequestResponseLog
        fields = (
            'path',
            'request_method',
            'time',
        )