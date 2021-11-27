from rest_framework import serializers
from api.models import CustomUser
from backend.settings import ACCOUNT_EMAIL_REQUIRED
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
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username',''),
            'email': self.validated_data.get('email',''),
            'password1': self.validated_data.get('password1','')
        }
    
    def save(self,request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request,user,self)
        self.custom_signup(request,user)
        setup_user_email(request,user,[])
        return user
    
        user.save()
        return user
        
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "last_name"
        )
        
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('email',)