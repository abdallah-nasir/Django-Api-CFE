import requests
from rest_framework import serializers

# import json
# BASE_DIR="http://127.0.0.1:8000/"  #where it will go
# END_POINT="updates/"

# def get_list():
#     r=requests.get(BASE_DIR + END_POINT)
#     data=r.json()
#     print(data["content"])
#     print(r.status_code)
#     # for i in data:
#     #     print(i["content"])
 
#     return data

# get_list()
# # print(get_list())

# def create_update(): 
#     dict={
#         "user":1,
#         "content":"asdad",}
#     r=requests.post(BASE_DIR + END_POINT,data=dict)
#     print(r.json())
# create_update()



class StatusSerializers(serializers.ModelSerializer):
    email=serializers.EmailField()
    
    def validate_email(self,value):
        if len(value) >10:
            raise serializers.ValidationError("more than 10 words")  

        return value

StatusSerializers()
data={"email":"asdssssssss"}
asdasd=StatusSerializers(data=data)

if asdasd.is_valid():
    print("true")
else:
    print("False")