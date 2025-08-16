from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)  # Increased max_length to 255
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # Added author field

    def __str__(self):
        return self.title