from django.urls import path
from .views import (
    create_article, get_articles, get_article, get_filterd_articles,
    get_excluded_articles, get_ordered_articles, get_field_lookups,
    get_aggregations_articles, filtered_articles, thankyou
)
from .views import ArticleCustomAPIView, ArticleModelAPIView, api_articles


urlpatterns = [
    path('create_article/', create_article, name='create_article'),
    path('get_articles/', get_articles, name='get_articles'),
    path('get_article/<int:id>', get_article, name='get_article'),
    path('get_filterd_articles/', get_filterd_articles, name='get_filterd_articles'),
    path('get_excluded_articles/', get_excluded_articles, name='get_excluded_articles'),
    path('get_ordered_articles/', get_ordered_articles, name='get_ordered_articles'),
    path('get_field_lookups/', get_field_lookups, name='get_field_lookups'),
    path('get_aggregations_articles/', get_aggregations_articles, name='get_aggregations_articles'),
    path('filtered_articles/', filtered_articles, name='filtered_articles'),
    path('api/articles/', api_articles, name='api_articles'),
    path('api/custom-articles/', ArticleCustomAPIView.as_view(), name='custom-article-api'),
    path('api/model-articles/', ArticleModelAPIView.as_view(), name='model-article-api'),
    path('thank-you/', thankyou, name='thank-you'),
]
