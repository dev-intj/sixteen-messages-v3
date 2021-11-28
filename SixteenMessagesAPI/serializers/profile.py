from rest_framework import serializers
from SixteenMessagesAPI.models import Profile
from .user import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source="user.username")
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    profile_image = serializers.ImageField(required=False)
    hide_name = serializers.BooleanField(required=True)
    hide_email = serializers.BooleanField(required=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "profile_image",
            "hide_name",
            "hide_email",
            "user"
        )