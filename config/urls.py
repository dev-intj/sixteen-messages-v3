from django.conf.urls import include,url
from django.urls import path
from rest_framework.routers import DefaultRouter
from SixteenMessagesAPI.viewsets import ProfileViewset,UserViewset
from allauth.account.views import confirm_email

router = DefaultRouter()

router.register(
    r"profile",ProfileViewset,basename="profile"
)

router.register(
    r"user",UserViewset,basename="user"
)

base_api_url = 'api/'

urlpatterns = [
    path('api/',include(router.urls)),
    path(f'{base_api_url}rest-auth/', include('rest_auth.urls')),
    path(f'{base_api_url}rest-auth/registration/', include('rest_auth.registration.urls')),
    path(f'{base_api_url}account/', include('allauth.urls')),
    path(f'{base_api_url}accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]