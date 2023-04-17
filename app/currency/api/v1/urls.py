# from django.urls import path
from currency.api.v1.views import RateViewSet, ContactUsViewSet, SourceViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api-currency'

router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rates')
router.register(r'contactus', ContactUsViewSet, basename='contactus')
router.register(r'sources', SourceViewSet, basename='sources')


urlpatterns = [
    # path('rates/', RateApiView.as_view(), name='rates'),
    # path('rates/<int:pk>/', RateDetailApiView.as_view(), name='rates-detail')
]

urlpatterns += router.urls
