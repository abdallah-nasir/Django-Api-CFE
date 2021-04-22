from django.test import TestCase
from django.contrib.auth import get_user_model 
from .models import Status
# Create your tests here.

User=get_user_model()



class StatusTestCase(TestCase):
    def setUp(self):
        user=User.objects.create(username="malek",email="malek@yahoo.com")  
        user.set_password("123456789Boss")
        user.save()


    def test_creaed_status(self):
        user=User.objects.get(username="malek")
        obj=Status.objects.create(user=user,content="bullshit")
        self.assertEqual(obj.id,1)
        qs=Status.objects.all()
        self.assertEqual(qs.count(),1)



























