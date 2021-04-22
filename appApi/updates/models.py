import json
from django.conf import settings 
from django.db import models
from django.core.serializers import serialize
# Create your models here.


def upload(instance,filename):
    return (f"api/updates/{instance.user}/{filename}")

class Update(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    image =models.ImageField(upload_to="upload",blank=True,null=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    # def serialize(self):
    #     json_data=serialize("json",[self])
    #     stuct=json.loads(json_data)
    #     data=json.dumps(stuct[0]["fields"])
    #     return data

    #another way 
    def serialize(self):
        data={
            "user":self.user.id,
            "user_name":self.user.username,
            "content":self.content,
            "image":self.image.url
            }
        data=json.dumps(data)
        return data
