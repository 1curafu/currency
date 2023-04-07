from django.contrib import admin
from currency.models import Rate, ContactUs, Source, RequestResponseLog

from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'currency',
        'source',
        'created',
    )
    list_filter = (
        'currency',
        ('created', DateRangeFilter),
    )
    search_fields = (
        'source',
        'buy',
        'sale',
    )


@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'email',
        'subject',
        'message',
    )
    list_filter = (
        'email',
    )
    search_fields = (
        'email',
        'subject',
        'message',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
        'country',
        'city',
    )
    list_filter = (
        'name',
        'country',
        'city',
    )
    search_fields = (
        'name',
        'source_url',
        'country',
        'city',
    )


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'path',
        'request_method',
        'time',
    )
    search_fields = (
        'request_method',
    )

    def has_add_permission(self, request):
        return False
