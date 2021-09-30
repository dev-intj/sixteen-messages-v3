from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class ProfileViewset(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = [DjangoFilterBackend]

class MessageViewset(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    filter_backends = [DjangoFilterBackend]