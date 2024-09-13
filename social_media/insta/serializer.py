from rest_framework.serializers import ModelSerializer
from .models import Post, Like, Comment, Follow

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FollowSerializer(ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'