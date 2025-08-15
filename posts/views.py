from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
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



class PostListCreateView(generics.GenericAPIView, 
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(APIView):
    serializer_class = PostSerializer

    