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

urlpatterns = [
    path("api/",include(router.urls)),
    path(r'rest-auth/', include('rest_auth.urls')),
    path(r'rest-auth/registration/', include('rest_auth.registration.urls')),
    path(r'account/', include('allauth.urls')),
    path(r'accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]