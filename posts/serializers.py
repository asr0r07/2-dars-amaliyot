from django.utils.text import slugify
from rest_framework import serializers
from .models import Post
from category.models import Category
from tags.models import Tag
from author.models import Author


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status']
        read_only_fields = ['slug']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def create(self, validated_data):
        category_id = self.initial_data.get('category')
        author_id = self.initial_data.get('author')
        tags_data = self.initial_data.get('tags', [])

        category = Category.objects.get(id=category_id)
        author = Author.objects.get(id=author_id)
        post = Post.objects.create(
            title=validated_data['title'],
            slug=slugify(validated_data['title']),
            content=validated_data['content'],
            category=category,
            author=author,
            status=validated_data.get('status', 'draft')
        )

        for tag_id in tags_data:
            tag = Tag.objects.get(id=tag_id)
            post.tags.add(tag)

        return post

    def update(self, instance, validated_data):
        category_id = self.initial_data.get('category')
        author_id = self.initial_data.get('author')
        tags_data = self.initial_data.get('tags', [])

        if category_id:
            instance.category = Category.objects.get(id=category_id)
        if author_id:
            instance.author = Author.objects.get(id=author_id)

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)

        instance.save()

        if tags_data:
            instance.tags.clear()
            for tag_id in tags_data:
                tag = Tag.objects.get(id=tag_id)
                instance.tags.add(tag)

        return instance
