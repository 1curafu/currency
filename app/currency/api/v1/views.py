from rest_framework import viewsets
from rest_framework import filters as rest_framework_filters

from currency.throttlers import AnonCurrencyThrottle
from currency.filters import RateAPIFilter, ContactUsAPIFilter, SourceAPIFilter
from currency.paginators import RatesPagination, ContactUsPagination, SourcePagination  # generics
from currency.models import Rate, Source, ContactUs
from currency.api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django_filters import rest_framework as filters


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer  # json.dumps, json.loads
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)  # json, xml, yaml
    pagination_class = RatesPagination  # PageNumberPagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )

    filterset_class = RateAPIFilter
    ordering_fields = ('id', 'created', 'buy', 'sale')
    search_fields = ('name', 'source__name')
    throttle_classes = (AnonCurrencyThrottle,)

    @action(detail=True, methods=['post'])
    def buy(self, request, *args, **kwargs):
        rate = self.get_object()
        sz = self.get_serializer(instance=rate)
        return Response(sz.data)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)  # json, xml, yaml
    pagination_class = ContactUsPagination  # PageNumberPagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )

    filterset_class = ContactUsAPIFilter
    ordering_fields = ('id', 'created', 'name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)  # json, xml, yaml
    pagination_class = SourcePagination  # PageNumberPagination
    permission_classes = (AllowAny,)
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = SourceAPIFilter
    ordering_fields = ('id', 'name', 'code_name')
    search_fields = ('name', 'code_name')
