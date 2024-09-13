from django.contrib.admin import register, ModelAdmin
from .models import Post , Comment , Like , Follow 
@register(Post)
class PostAdmin(ModelAdmin):
    readonly_fields=['sum_like_count']
    list_display = [
        'user','image','text','created_at'
    ]

@register(Comment)
class CommentAdmin(ModelAdmin):...


@register(Follow)
class FollowAdmin(ModelAdmin):...


@register(Like)
class LikeAdmin(ModelAdmin):...
# Register your models here.
