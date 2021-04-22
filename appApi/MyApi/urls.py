from django.urls import path
from .views import *

app_name="MyApi"

urlpatterns = [
path("",ListApi.as_view()),   
path("details/<pk>/",DetailApi.as_view(),name="posts"),
# path("user/details/<username>/",UserDetailApi.as_view(),name="user"),


]
