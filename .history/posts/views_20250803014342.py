from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

# Create your views here.
def homepage(response:HttpRequest):
    response = {"message":"Hello world"}
    return JsonResponse(data=response)
