from django import forms

from currency.models import Rate, ContactUs, Source, RequestResponseLog


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'currency',
            'buy',
            'sale',
            'source'
        )


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
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
            'city',
            'avatar',
        )


class RequestResponseLogForm(forms.ModelForm):
    class Meta:
        model = RequestResponseLog
        fields = (
            'path',
            'request_method',
            'time',
        )
