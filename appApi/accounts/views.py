from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate,get_user_model
from rest_framework_jwt.settings import api_settings
from .serializers import *
# Create your views here.

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler=api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User=get_user_model()

class RegisterApi(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegister
    permission_classes=[AllowAny]

# class AuthView(APIView):
#     permission_classes=[AllowAny]
#     def post(self,request,*args,**kwargs):
#         print(request.user)
#         if request.user.is_authenticated:
#             return Response({"details":"ayou are logged in"},status=400)
#         data=request.data
#         username=data.get("username")
#         password=data.get("password")
#         user=authenticate(username=username,password=password)
#         payload = jwt_payload_handler(user) #this is to create your token manually
#         token = jwt_encode_handler(payload)#this is to create your token manually
#         response=jwt_response_payload_handler(token,user,request=request)
#         print(user)
#         return Response(response)