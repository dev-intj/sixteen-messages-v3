from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from api.viewsets import ProfileViewset,MessageViewset,AccountViewset

router = routers.SimpleRouter()

router.register('message',MessageViewset)
router.register('profile',ProfileViewset)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/account/register',AccountViewset.as_view(),name="register"),
    path('admin/', admin.site.urls),
]