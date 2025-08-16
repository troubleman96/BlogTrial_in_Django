from . import views
from django.urls import path
from .views import ListPostsView

"""urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.PostListCreateView.as_view(), name="list_posts"), #as_view to call it as function
    path("<int:pk>/", views.PostRetrieveUpdateDeleteView.as_view(), name="retrieve_update_delete_post"),
]"""


urlpatterns = [
    path("posts_for_current/", ListPostsView.as_view(), name="posts-for-current"),
]