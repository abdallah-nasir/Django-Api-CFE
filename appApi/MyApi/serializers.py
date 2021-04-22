from .models import *
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField,ModelSerializer
from accounts.serializers import Username


class StatusSerializers(ModelSerializer):
    user=Username(read_only=True)
    class Meta:
        model=Status
        fields=["user","content","image"]
        read_only_fields=["user"]

    def validate_content(self,value):
        if len(value) >10:
            raise serializers.ValidationError("more than 10 words")  

        return value
        
    # def validate(self,data):
    #     if len(value) >10:
    #         raise serializers.ValidationError("more than 10 words")  
    #     return data

post_detail_url = HyperlinkedIdentityField(view_name='api:posts',lookup_field="pk")
# user_detil_url=HyperlinkedIdentityField(view_name='api:user',lookup_field="username")
class StatusListSerializers(ModelSerializer):
    details=post_detail_url
    # user_id=serializers.PrimaryKeyRelatedField(source="user",read_only=True)
    # user=Username(read_only=True)
    user=serializers.SlugRelatedField(read_only=True,slug_field="username")
    # email=serializers.SlugRelatedField(source="user",read_only=True,slug_field="email")
    class Meta:
        model=Status
        fields=["user","content","image","details"]
        read_only_fields=["user"]

