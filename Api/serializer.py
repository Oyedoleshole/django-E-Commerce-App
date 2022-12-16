from rest_framework import serializers
from Api.models import User, UserModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import api_view

#Serializer to register User
class RegisterSerializer(serializers.ModelSerializer):
    email= serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password= serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2= serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name','id')
        extra_kwargs = {'first_name':{'required':True},'last_name':{'required':True}}

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password Field does'nt match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email= validated_data['email'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

#Serializer to Login the User
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=200)
    class Meta:
        model=User
        fields=['email', 'password']

class DetailSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=200)
    first_name=serializers.CharField(max_length=200)
    last_name=serializers.CharField(max_length=200)
    class Meta:
        model =User
        fields = ['id', 'first_name', 'last_name', 'email']

#These Things were added by me 16-Nov-2022.


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MessageModel(models.Model):
    email =  models.EmailField(max_length=200 )
    name = models.CharField(max_length=200 )
    subject = models.CharField(max_length=200)
    phone = models.BigIntegerField(null=True)
    message = models.CharField(max_length=200 )

    def __str__(self):
        return self.name

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ['name', 'email', 'subject', 'phone', 'message']
        

class RegisterUser(models.Model):
    email=models.EmailField(unique=True, max_length=20)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegisterUser
        fields=['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields = ['id','first_name','last_name', 'email']