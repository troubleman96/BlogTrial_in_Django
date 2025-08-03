from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
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



class PostListCreateView(APIView):
    serializer_class = PostSerializer

    def get(self, request:Request, *args, **kwags):
        posts = Post.objects.all() #fetching from db

        serializer = self.serializer_class(instance=posts, many=True) #serializing, many to convert to list

        response = {
            "message":"posts", "data":serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request:Request, *args, **kwags):
        data = request.data #data from the request

        serializer = self.serializer_class(data=data) #serializing

        if serializer.is_valid():
            serializer.save() #to db

            response = {
                "message":"post created", "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveUpdateDeleteView(APIView):
    serializer_class