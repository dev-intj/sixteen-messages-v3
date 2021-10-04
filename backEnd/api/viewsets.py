from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt

class ProfileViewset(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = [DjangoFilterBackend]

class MessageViewset(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    filter_backends = [DjangoFilterBackend]

class AccountViewset(APIView):
    @csrf_exempt
    def post(self,request):
        serializer = serializers.RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['id'] = account.id
        else:
            data = serializer.errors
        return Response(data)