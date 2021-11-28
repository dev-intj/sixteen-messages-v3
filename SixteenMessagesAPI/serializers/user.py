from rest_framework import serializers
from SixteenMessagesAPI.models import CustomUser

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    
    def validate_password1(self,password):
        return get_adapter().clean_password(password)
    
    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match.")
            )
        return data
        
    class Meta:
        model = CustomUser
        fields = '__all__'
        
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('email',)