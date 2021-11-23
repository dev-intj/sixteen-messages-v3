from rest_framework import serializers

from api.models.models import Profile,Message,Account

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'},write_only=True)
    class Meta:
        model = Account
        fields = ['email','password','password2']
        extra_kwards = {
            'password' : {'write_only':True}
        }
    
    def save(self):
        account = Account(
            email = self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        account.save()
        return account