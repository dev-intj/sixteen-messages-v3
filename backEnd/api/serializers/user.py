from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "last_name"
        )