from rest_framework import serializers
from .models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    # Override the to_representation method to combine first_name and last_name
    def to_representation(self, instance):
        # Return the full name as a single string
        return f"{instance.first_name} {instance.last_name}"

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
