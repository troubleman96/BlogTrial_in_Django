from rest_framework.request import Request
from rest_framework.response import Response



def homepage(request:Request):
    response={"message": "Hellow World"}
    return (data=response, sta)