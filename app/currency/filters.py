import django_filters
from currency.models import Rate, Source, ContactUs, RequestResponseLog


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = ['buy', 'sale', 'source']


class RateAPIFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sale': ('gt', 'gte', 'lt', 'lte', 'exact'),
        }


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = ['name', 'country']


class SourceAPIFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = {
            'name': ('icontains', 'istartswith', 'iendswith', 'iexact'),
            'country': ('icontains', 'istartswith', 'iendswith', 'iexact'),
        }


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = ['name', 'subject']


class ContactUsAPIFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'name': ('icontains', 'istartswith', 'iendswith', 'iexact'),
            'subject': ('icontains', 'istartswith', 'iendswith', 'iexact'),
        }


class RequestResponseLogFilter(django_filters.FilterSet):

    class Meta:
        model = RequestResponseLog
        fields = ['request_method']
