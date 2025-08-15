from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import SignupSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .tokens import create_jwt_tokens

class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]  # <-- Add this line

    def post(self,request:Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response={
            "message": "User registered successfully.",
            "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]  # <-- Add this line

    def post(Self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            # User is authenticated

            tokens = create_jwt_tokens(user)

            content = {
                "message": "Login successful",
                "tokens": tokens
            }
            return Response(data=content, status=status.HTTP_200_OK)
        
        else:
            return Response(data={
                "message": "invcalid credentials"
            })
            

    def get(Self, request:Request):
        content = {
            "user": str(request.user),  # `user` is a User object
            "auth": str(request.auth)  # `auth` is a Token object if using TokenAuthentication
        }
        return Response(data=content, status=status.HTTP_200_OK)

