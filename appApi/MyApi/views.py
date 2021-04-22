from django.shortcuts import render
from rest_framework.generics import (
ListAPIView,
CreateAPIView,
RetrieveAPIView,
UpdateAPIView,
DestroyAPIView,
RetrieveUpdateDestroyAPIView,
ListCreateAPIView,
RetrieveUpdateDestroyAPIView
) 
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *
from .models import *
from accounts.permissions import IsOwnerOrReadOnly
# Create your views here.


class ListApi(ListCreateAPIView):
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # authentication_classes=[SessionAuthentication,BasicAuthentication]
    queryset =Status.objects.all()
    serializer_class=StatusListSerializers
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['user__username',"user__id", 'content']
    ordering_fields = ["timestamp"]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    # lookup_field = "id"

    # def get_queryset(self):
    #     qs=Status.objects.all()
    #     query=self.request.GET.get("q")
    #     if query is not None:
    #         qs=qs.filter(content__icontains=query)
    #     return qs

class DetailApi(RetrieveUpdateDestroyAPIView):
    queryset =Status.objects.all()
    serializer_class=StatusSerializers
    lookup_field = "pk"
    permission_classes=[IsOwnerOrReadOnly]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

# class UserDetailApi(ListCreateAPIView):
#     # queryset =Status.objects.filter(user=request.user)
#     serializer_class=StatusSerializers
#     # lookup_field = "username"
#     permission_classes=[IsOwnerOrReadOnly]

#     def get_queryset(self):
#         qs=Status.objects.filter(user=self.request.user)
#         return qs
        