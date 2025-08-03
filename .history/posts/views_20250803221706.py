from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404





@api_view(http_method_names=["GET"])
def post_detail(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id) #shortcut for fetching the product

    serializer = PostSerializer(instance=post)

    response = {
        "message":"post", "data":serializer.data
    }
  
    return Response(data=response, status=status.HTTP_200_OK)

class PostListCreateView()

@api_view(http_method_names=["PUT"])
def update_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id) #fetching the data from db shorcut w 404
    
    data = request.data #getting the inputted data from request
    
    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save() #save data/update to db

        response ={
            "message": "Post Updated sucessfully!",
            "data":serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["DELETE"])
def delete_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)

    post.delete() #delete the data from db 

    return Response(status=status.HTTP_204_NO_CONTENT)