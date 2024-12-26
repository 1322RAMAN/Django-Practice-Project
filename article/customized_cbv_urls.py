from django.urls import path
from .customized_cbv_views import (
    ContactFormView,
    CustomArticleCreateView,
    CustomContextArticleListView,
    FilteredArticleListView,
    UserArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ContactAuthorView,
    PaginatedArticleListView
)

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('custom_article_create/', CustomArticleCreateView.as_view(), name='custom_article_create'),
    path('custom_article_list/', CustomContextArticleListView.as_view(), name='custom_article_list'),
    path('filtered_article_list/', FilteredArticleListView.as_view(), name='filtered_article_list'),
    path('user_article_list/', UserArticleListView.as_view(), name='user_article_list'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='custom_article_detail'),
    path('article_update/<int:pk>/', ArticleUpdateView.as_view(), name='custom_article_update'),
    path('article_delete/<int:pk>/', ArticleDeleteView.as_view(), name='custom_article_delete'),
    path('articles/<int:pk>/contact/', ContactAuthorView.as_view(), name='contact_author'),
    path('paginated_article_list/', PaginatedArticleListView.as_view(), name='paginated_article_list'),
]
