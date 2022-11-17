from asyncore import write
from email import message
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField(max_length=20,validators=[UniqueValidator(queryset=User.objects.all(), message=("Username alredy in use"))])
    email=serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message=("Username alredy in use"))])
    birthdate=serializers.DateField()
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    password=serializers.CharField(write_only=True)
    bio=serializers.CharField(allow_null=True,allow_blank=True, required=False)
    is_critic=serializers.BooleanField(default=False, required=False)
    is_superuser=serializers.BooleanField(default=False, required=False)
    updated_at= serializers.DateTimeField(required=False)
     
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)    
