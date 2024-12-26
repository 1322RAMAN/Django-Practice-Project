from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView   # Import the required views
from django.views.generic import TemplateView
from django.urls import reverse_lazy  # Import reverse_lazy for redirecting to a URL after form submission
from .models import Article


class MyView(View):
    """View: Basic Class-Based View
    Use Case: Custom logic for specific HTTP methods.
    """
    def get(self, request):
        return HttpResponse('GET response')

    def post(self, request):
        return HttpResponse('POST response')


class HomePageView(TemplateView):
    """TemplateView: Render Static Templates
    Use Case: Display a simple static page with optional context.
    """
    # Example: Render a Home Page with Context.
    template_name = 'article/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to My Website Home Page'  # Add custom context data
        return context


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/article_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('article_list')  # Redirect to the article list view after successful creation


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list2.html'  # Specify the template
    context_object_name = 'articles'  # The name of the context variable in the template
    queryset = Article.objects.all().order_by('-pub_date')  # Order articles by publication date


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail2.html'  # Specify the template
    context_object_name = 'article'  # The name of the context variable in the template


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/article_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
