from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


posts = [
    {
        "id":1,
        "title": "learn programming",
        "content": "a full lesson on drf"
    },
{
        "id":2,
        "title": "rust programming",
        "content": "a short lesson on fastapi"
    },
    {
        "id":3,
        "title": "java programming",
        "content": "a full course on kotlin"
    }
]

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