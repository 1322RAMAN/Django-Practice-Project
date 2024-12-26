"""
Django's Generic Class-Based Views (GCBVs) provide a powerful and reusable way to handle common web application tasks like creating,
retrieving, updating, and deleting objects. GCBVs allow you to write less code by using pre-built views that handle the majority of the
logic for you, with customization options where necessary.
Here's an in-depth look at all the common Generic Class-Based Views in Django, with detailed examples.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Article
from .custom_serializers import ArticleCustomSerializer


class ArticleListView(generics.ListAPIView):
    """List View (ListAPIView): This view is used to list all the articles."""
    queryset = Article.objects.all()  # Queryset to get all articles
    serializer_class = ArticleCustomSerializer  # Serializer to use for serializing article data

    def get(self, request, *args, **kwargs):
        """Retrieve all articles."""
        return super().get(request, *args, **kwargs)


class ArticleCreateView(generics.CreateAPIView):
    """Create View (CreateAPIView): This view is used to create a new article."""
    queryset = Article.objects.all()  # Queryset to create articles
    serializer_class = ArticleCustomSerializer  # Serializer to validate and save article data
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def perform_create(self, serializer):
        """Override to save the current user as the author."""
        serializer.is_valid(raise_exception=True)  # Ensure data is validated
        serializer.save()


class ArticleRetrieveView(generics.RetrieveAPIView):
    """Retrieve View (RetrieveAPIView): This view is used to retrieve the details of a single article."""
    queryset = Article.objects.all()  # Queryset to retrieve a specific article
    serializer_class = ArticleCustomSerializer  # Serializer for serializing article data
    lookup_field = 'id'  # Look up the article by its ID

    def get(self, request, *args, **kwargs):
        """Retrieve a single article."""
        return super().get(request, *args, **kwargs)


class ArticleUpdateView(generics.UpdateAPIView):
    """Update View (UpdateAPIView): This view is used to update an existing article."""
    queryset = Article.objects.all()  # Queryset to update articles
    serializer_class = ArticleCustomSerializer  # Serializer for validating and saving article data
    lookup_field = 'id'  # Look up the article by its ID

    def perform_update(self, serializer):
        """Override to automatically set the author to the logged-in user if not provided."""
        if not serializer.validated_data.get('author'):  # Check if author is not provided
            serializer.validated_data['author'] = self.request.user  # Set author to logged-in user
        serializer.save()


class ArticleDeleteView(generics.DestroyAPIView):
    """Delete View (DestroyAPIView): This view is used to delete an article."""
    queryset = Article.objects.all()  # Queryset to delete the article
    lookup_field = 'id'  # Look up the article by its ID

    def delete(self, request, *args, **kwargs):
        """Delete an article."""
        return super().delete(request, *args, **kwargs)


class ArticleListCreateView(generics.ListCreateAPIView):
    """List and Create View (ListCreateAPIView): This view combines both ListAPIView and CreateAPIView,
        meaning it can be used for listing articles and creating new articles."""
    queryset = Article.objects.all()  # Queryset to list and create articles
    serializer_class = ArticleCustomSerializer  # Serializer for serializing and validating article data

    def perform_create(self, serializer):
        """Override to set the logged-in user as the author."""
        serializer.save(author=self.request.user)  # Automatically set the logged-in user as author


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update, and Delete View (RetrieveUpdateDestroyAPIView):
        This view combines RetrieveAPIView, UpdateAPIView, and DestroyAPIView,
        allowing retrieval, updating, and deletion of a single article.
    """
    queryset = Article.objects.all()  # Queryset to retrieve, update, and delete articles
    serializer_class = ArticleCustomSerializer  # Serializer for serializing and validating article data
    lookup_field = 'id'  # Look up the article by its ID
