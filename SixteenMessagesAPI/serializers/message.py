from rest_framework import serializers
from SixteenMessagesAPI.models import Message

class MessageSerializer(serializers.ModelSerializer):
    profile = serializers.IntegerField()
    unique_id = serializers.UUIDField()
    message = serializers.CharField(required=True)
    show_user = serializers.BooleanField(required=True)
    can_be_shared = serializers.BooleanField(required=True)
    
    class Meta:
        model = Message
        fields = (
            "id",
            "profile",
            "unique_id",
            "message",
            "show_user",
            "can_be_shared",
        )