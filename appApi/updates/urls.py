from django.urls import path
from . import views
from .views import *
app_name="updates"

urlpatterns = [
    # path('updates/',JsonCbv2.as_view(),name="update"),
    # path('', JoinFormView.as_view()),
    path('',views.JoinFormView),

]