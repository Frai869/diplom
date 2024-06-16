from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'USER: {self.user} POST: {self.text}')

    def likes_count(self):
        return self.likes.count()

# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    like = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return (f'POST: {self.post.text} USER: {self.user} LIKE: {self.like}')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return (f'POST: {self.post.text} USER: {self.user} COMMENT: {self.text}')