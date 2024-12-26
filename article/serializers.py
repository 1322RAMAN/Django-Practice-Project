from rest_framework import serializers
from .models import Article


# ModelSerializer: Automatically handles serialization/deserialization for Django models, reducing boilerplate code.
class ArticleModelSerializer(serializers.ModelSerializer):
    """ Automatically handles serialization/deserialization for Django models, reducing boilerplate code. """
    class Meta:
        model = Article
        fields = '__all__'  # You can also list specific fields like ['title', 'content', 'author']
