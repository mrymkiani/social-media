from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    likes_count = models.PositiveIntegerField(default=0)  # تعداد لایک‌ها
    comments_count = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.user.first_name
    
    
    @property
    def sum_like_count(self):
        return self.like.count()
    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "My Posts"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    post = models.ForeignKey(Post, on_delete=models.CASCADE  , related_name="like")
    
        

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.follower.first_name