from rest_framework import serializers
from .models import Fakulteti,Departamenti,Programi,Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user





class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()

class FakultetiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakulteti
        fields = ['id', 'emertimi']

class DepartamentiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Departamenti
        fields = ['id', 'emertimi','fakulteti']

class ProgramiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programi

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile



        