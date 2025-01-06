from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db.models import Count, Max, Min, Avg
from django.views import View
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleModelSerializer
# from .custom_serializers import ArticleCustomSerializer
from .forms import ArticleForm
from .models import Article


# Function-based views (FBV)
def home(request):
    return render(request, 'article/home.html', {'name': 'Django User'})


def thankyou(request):
    return render(request, 'article/thank_you.html')


# Class-based views (CBV)
class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the homepage (CBV)!")


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'article/thank_you.html')
    else:
        form = ArticleForm()
    return render(request, 'article/create_article.html', {'form': form})


def get_articles(request):
    """ Retrieve all objects """
    articles = Article.objects.all().values()
    return render(request, 'article/articles.html', {'articles': articles})


def get_article(request, id):
    """ Retrieve a single object by ID """
    # article = Article.objects.get(id=1)
    article = Article.objects.get(id=id)
    return HttpResponse(article)


def get_filterd_articles(request):
    """ Filter objects """
    recent_articles = Article.objects.filter(pub_date__year=2024)
    return HttpResponse(f"recent_articles = {recent_articles}")


def get_excluded_articles(request):
    """ Exclude objects """
    not_recent = Article.objects.exclude(pub_date__year=2024)
    return HttpResponse(f"not_recent = {not_recent}")


def get_ordered_articles(request):
    """ Ordering """
    ordered_articles = Article.objects.order_by('-pub_date')
    recent_and_ordered = Article.objects.filter(pub_date__year=2024).order_by('-pub_date')
    print('------- recent_and_ordered -------', recent_and_ordered)
    return HttpResponse(f"ordered_articles = {ordered_articles}")


def get_field_lookups(request):
    """ Field Lookups """
    # Exact match
    articles = Article.objects.filter(title__exact="First Article")
    print('------- articles ------', articles)

    # Case-insensitive match
    articles2 = Article.objects.filter(title__iexact="first article")
    print('------- articles2 ------', articles2)

    # Contains
    articles3 = Article.objects.filter(content__contains="Django")
    print('------- articles3 ------', articles3)

    # Greater than
    articles4 = Article.objects.filter(pub_date__gt="2024-01-01")
    print('------- articles4 ------', articles4)
    return HttpResponse('Field Lookups !')


def get_aggregations_articles(request):
    """ Using Aggregates Django provides aggregation functions like Sum, Avg, Count, etc. """
    article_stats = Article.objects.aggregate(
        total_articles=Count('id'),
        latest_pub_date=Max('pub_date'),
        earliest_pub_date=Min('pub_date'),
        avg_pub_date=Avg('id')
    )
    print('------- article_stats --------', article_stats)
    return HttpResponse('Aggregates Articles !')


def filtered_articles(request):
    """ Create dynamic filters based on user input: """
    search_query = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=search_query)
    print('-------- articles --------', articles)
    return render(request, 'article/article_detail.html', {'articles': articles})


@api_view(['GET'])
def api_articles(request):
    articles = Article.objects.all()
    serializer = ArticleModelSerializer(articles, many=True)
    return Response(serializer.data)


class ArticleModelAPIView(APIView):
    def get(self, request):
        """Retrieve all articles."""
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new article."""
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def query_optimization(request):
    # Inefficient Query
    articles = Article.objects.all()
    for article in articles:
        print('Inefficient Query', article.author.first_name)
    # Efficient Query
    articles = Article.objects.select_related('author').all()
    for article in articles:
        print('Efficient Query', article.author.first_name)

    articles = Article.objects.only('title', 'content')
    for article in articles:
        print('Fetch only required fields - ', article.title)
    return HttpResponse("Query Optimization !")
