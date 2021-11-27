from django.contrib.auth import get_user_model
from ..serializers import UserSerializer
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import get_serializer_class, swagger_auto_schema

class UserViewset(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,
        ):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def list(self,request,*args, **kwargs):
        serializer = UserSerializer(many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(True)
        user = serializer.save(self)
        return Response(data=user,status=status.HTTP_200_OK)
