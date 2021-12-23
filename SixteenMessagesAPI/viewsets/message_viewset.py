from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from ..models import Message
from ..serializers import MessageSerializer

class MessageViewset(viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer