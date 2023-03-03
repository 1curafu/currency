
from django.urls import path

from currency.views import (

    RateListView,
    RateDetailView,
    RateCreateView,
    RateDeleteView,
    RateUpdateView,
    ContactUsListView,
    ContactUsDetailView,
    ContactUsCreateView,
    ContactUsUpdateView,
    ContactUsDeleteView,
    SourceListView,
    SourceDetailView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
)

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/detail/<int:pk>/', RateDetailView.as_view(), name='rate-detail'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('contact/list/', ContactUsListView.as_view(), name='contact-list'),
    path('contact/create/', ContactUsCreateView.as_view(), name='contact-create'),
    path('contact/detail/<int:pk>/', ContactUsDetailView.as_view(), name='contact-detail'),
    path('contact/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contact-update'),
    path('contact/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contact-delete'),

    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-detail'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
]
