from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from api.viewsets import ProfileViewset,MessageViewset

router = routers.SimpleRouter()

router.register('message',MessageViewset)
router.register('profile',ProfileViewset)

urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),
]