from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_email', 'content', 'created_at', 'parent_comment', 'replies']

    def get_replies(self, obj):
        replies = obj.replies.all()
        return CommentSerializer(replies, many=True).data if replies.exists() else None

    def validate_parent_comment(self, value):
        if value and value.parent_comment and value.parent_comment.parent_comment:
            raise serializers.ValidationError("Only 3 levels of nested comments are allowed.")
        return value
