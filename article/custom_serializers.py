from rest_framework import serializers
from .models import Article


class ArticleCustomSerializer(serializers.ModelSerializer):
    """Custom serializer for the Article model."""

    author = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'pub_date', 'created_at', 'updated_at']
        read_only_fields = ['author', 'pub_date', 'created_at', 'updated_at']  # Fields that shouldn't be updated

    def get_author(self, obj):
        """Customize the author field representation."""
        return {
            'id': obj.author.id,
            'name': f"{obj.author.first_name} {obj.author.last_name}".strip(),  # Combine first and last nameto get the Full Name
            'email': obj.author.email,
        }

    def create(self, validated_data):
        """Override the create method to handle author assignment."""
        request = self.context.get('request')
        if 'author' not in validated_data:
            validated_data['author'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Override the update method to handle partial updates."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
