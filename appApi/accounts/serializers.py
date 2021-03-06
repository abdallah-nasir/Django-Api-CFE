from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.conf import settings
import datetime
from django.utils import timezone

expire_date=settings.JWT_AUTH["JWT_REFRESH_EXPIRATION_DELTA"]
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler=api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User=get_user_model()

class Username(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username"]

class UserRegister(serializers.ModelSerializer):
    password=serializers.CharField(style={"input_type":"password"},write_only=True)
    password2=serializers.CharField(style={"input_type":"password"},write_only=True)
    token =serializers.SerializerMethodField(read_only=True)
    expires =serializers.SerializerMethodField(read_only=True)

    class Meta:
        model =User
        fields=[
            "username",
            "email",
            "password",
            "password2",
            "token",
            "expires",
        ]
        extra_kwargs={"password":{"write_only":True}}
 
    def validate(self,data):
        pw=data.get("password")
        pw2=data.get("password2")
        if pw !=pw2:
            raise serializers.ValidationError("Passwords dosen't Match")
        return data


    def create(self,validated_data):
        obj=User(username=validated_data.get("username"),
        email=validated_data.get("email"))
        obj.set_password(validated_data.get("password"))
        obj.save()
        return obj

    def get_expires(self,obj):
        return timezone.now() + expire_date - datetime.timedelta(seconds=200)

    def get_token(self,obj):
        user = obj
        payload=jwt_payload_handler(user)
        token=jwt_encode_handler(payload)
        return token

