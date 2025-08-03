from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer



@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data    

        response={"message": "Hellow World", "data":data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    
    response={"message": "Hellow World"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def list_posts(request:Request):
    
    return Response(data=posts, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def post_detail(request:Request, post_index:int):
    post = posts[post_index]

    if post:
        return Response(data=post, status=status.HTTP_200_OK)
    
    return Response(data={"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)