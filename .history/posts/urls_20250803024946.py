from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.list_posts, name="list_posts"),
    path("detail/", views.post_detail, name="post_detail"),
]