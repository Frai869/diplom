from rest_framework import serializers
from posts.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ['user', 'text', 'created_at']
        fields = ['id', 'user', 'post', 'text', 'created_at',]
        read_only_fields = ['user', ]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'created_at', 'comments', 'likes_count',]
        read_only_fields = ['user',]