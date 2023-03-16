from django.urls import path

app_name = 'account'

from account.views import (
    UserSignUpView,
    UserActivateView
)

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>/', UserActivateView.as_view(), name='activate'),
]
