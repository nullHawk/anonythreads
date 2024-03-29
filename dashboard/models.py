from django.db import models
from django.contrib.auth.models import User

class Confession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    likes_users = models.ManyToManyField(User, related_name='liked_confessions')
    dislikes_users = models.ManyToManyField(User, related_name='disliked_confessions')

    def __str__(self):
        return f"{self.subject} by {self.user.username}"