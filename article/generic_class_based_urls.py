from django.urls import path

from .generic_class_based_views import (
    ArticleListView,
    ArticleCreateView,
    ArticleRetrieveView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleListCreateView,
    ArticleRetrieveUpdateDestroyView
)

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/create/', ArticleCreateView.as_view(), name='article-create'),
    path('articles/<int:id>/', ArticleRetrieveView.as_view(), name='article-detail'),
    path('articles/<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('articles/<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('articles/list-create/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:id>/retrieve-update-destroy/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-retrieve-update-destroy'),
]
