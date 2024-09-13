# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, Comment, Post

@receiver(post_save, sender=Like)
def update_post_likes_count(sender, instance, created, **kwargs):
    if created:
        instance.post.likes_count += 1
        instance.post.save()

@receiver(post_delete, sender=Like)
def update_post_likes_count_on_delete(sender, instance, **kwargs):
    instance.post.likes_count -= 1
    instance.post.save()

@receiver(post_save, sender=Comment)
def update_post_comments_count(sender, instance, created, **kwargs):
    if created:
        instance.post.comments_count += 1
        instance.post.save()

@receiver(post_delete, sender=Comment)
def update_post_comments_count_on_delete(sender, instance, **kwargs):
    instance.post.comments_count -= 1
    instance.post.save()