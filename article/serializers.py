from rest_framework import serializers
from article.models import Article
from user.serializers import AuthorSerializer


# ModelSerializer: Automatically handles serialization/deserialization for Django models, reducing boilerplate code.
class ArticleModelSerializer(serializers.ModelSerializer):
    """ Automatically handles serialization/deserialization for Django models, reducing boilerplate code. """
    class Meta:
        model = Article
        fields = '__all__'  # You can also list specific fields like ['title', 'content', 'author']


# Article Serializer with Nested Author Serializer:
class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = ['title', 'content', 'author']
