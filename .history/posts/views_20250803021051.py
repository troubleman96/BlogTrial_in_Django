from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


def homepage(request:Request):
    response={"message": "Hellow World"}
    return(data=response, status=status.Htt)