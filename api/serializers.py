from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', )
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'post', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, value):
        request = self.context['request']
        if Follow.objects.filter(user=request.user).filter(following=value).exists():
            raise serializers.ValidationError("Вы уже подписаны на этого автора")
        return value


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', )
        model = Group
