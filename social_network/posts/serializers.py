from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from posts.models import Comment, Post, Like


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'text', 'created_at', ]
        read_only_fields = ['user', ]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'image', 'created_at', 'comments', 'likes_count', ]
        read_only_fields = ['user', ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'like', ]
        read_only_fields = ['user', ]

    def validate(self, data):
        user = self.context['request'].user
        if Like.objects.filter(post_id=data['post'].id, user=user).exists():
            raise ValidationError('You liked this post already! Thank you!')
        return data