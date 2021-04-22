import requests
import json
ENDPOINT="http://127.0.0.1:8000/api/details/"

REFRESH_ENDPOINT="http://127.0.0.1:8000/accounts/api-token-refresh/"

AUTH_ENDPOINT="http://127.0.0.1:8000/accounts/"

headers={
    "Content-Type":"application/json"
}
data={"username":"abdallah",
"password":"12345s67a89Boss",
"password2":"asd"}
r=requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)
token=r.json()
print(token)
# def do(method="get",data={},id=1):
#     r=requests.request(method,ENDPOINT+str(id),data=data)
#     print(r.text)
#     return r


# do(data={"id":1,"content":"my content"})                                                                                                              