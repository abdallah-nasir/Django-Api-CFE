from django.urls import path
from .views import *
from rest_framework_jwt.views import (
refresh_jwt_token,
obtain_jwt_token,  #if you have accounts app put it there
verify_jwt_token)

app_name="accounts"

urlpatterns = [
    path("",RegisterApi.as_view(),name="accoun"),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    ]



