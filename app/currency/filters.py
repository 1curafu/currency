import django_filters
from currency.models import Rate, Source, ContactUs, RequestResponseLog


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = ['buy', 'sale', 'currency', 'source']


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', 'country']


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = ['email']


class RequestResponseLogFilter(django_filters.FilterSet):

    class Meta:
        model = RequestResponseLog
        fields = ['request_method']
