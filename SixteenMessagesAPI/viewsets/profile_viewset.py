from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from ..models import Profile
from ..serializers import ProfileSerializer,UserSerializer

class ProfileViewset(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(True)
        
        profile=serializer.save()
        
        if profile:
            return Response(
                ProfileSerializer(instance=profile).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)