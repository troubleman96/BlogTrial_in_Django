from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404



@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data    

        response={"message": "Hellow World", "data":data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    
    response={"message": "Hellow World"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST"])
def list_posts(request:Request):
    posts = Post.objects.all() #fetching data from db

    if request.method == "POST":
        data = request.data

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response={
                "message":"Post created",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(instance=posts, many=True)
    
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def post_detail(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id) #shortcut for fetching the product

    serializer = PostSerializer(instance=post)

    response = {
        "message":"post", "data":serializer.data
    }
  
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
def update_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)
    
    data = request.data
    
    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        


@api_view(http_method_names=["DELETE"])
def delete_post(request:Request, post_id:int): 
