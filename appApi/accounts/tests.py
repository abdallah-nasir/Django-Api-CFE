from django.test import TestCase
from rest_framework import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model 
from .models import Status
# Create your tests here.

User=get_user_model()



class StatusTestCase(APITestCase):
    def setUp(self):
        user=User.objects.create(username="malek",email="malek@yahoo.com")  
        user.set_password("123456789Boss")
        user.save()


    def test_creaed_user(self):
        qs=User.objects.get(username="malek")
        self.assertEqual(qs.count(),1)

    # def test_creaed_user_api(self):
    #   url= reverse("api:account")
    #   data={
    #     "username":"ahmed",
    #     "password1":"anypass",
    #     "email":"any@yahoo.com",
    #     "password2":"anypass",
    #   }
    #   response()























