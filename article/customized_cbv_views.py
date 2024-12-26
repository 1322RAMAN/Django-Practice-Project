from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView   # Import the required views
from .models import Article
from django.urls import reverse_lazy  # Import reverse_lazy for redirecting to a URL after form submission
from django.http import HttpResponse  # Import HttpResponse for returning HTTP responses
from django.http import HttpResponseForbidden  # Import HttpResponseForbidden for returning 403 Forbidden responses
# FormView
from django.views.generic.edit import FormView
from .forms import ContactForm, ContactAuthorForm
# RedirectView
# from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin  # Ensures that a view is only accessible to authenticated users.
from django.contrib.auth.mixins import PermissionRequiredMixin  # Ensures that a view is only accessible to users with specific permissions.
from .mixins import LoggingMixin  # Custom mixin for logging
from .mixins import OwnerRequiredMixin  # Custom mixin for Restricts access to views to the object's owner.


class CustomArticleCreateView(LoginRequiredMixin, CreateView):
    """
    Handles valid form submissions.
    Scenario: Automatically assign the logged-in user as the article author.
    """
    model = Article
    fields = ['title', 'content']
    template_name = 'article/article_form.html'
    success_url = reverse_lazy('custom_article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user  # Add logged-in user as author
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Invalid form submission. Please try again.")


class FilteredArticleListView(LoginRequiredMixin, ListView):
    """Used in views like ListView to customize the queryset."""
    model = Article
    template_name = 'article/article_list3.html'
    context_object_name = 'articles'  # The name of the context variable in the template

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)    # Filter articles by the logged-in user


class CustomContextArticleListView(LoginRequiredMixin, ListView):
    """Add custom context data to templates."""
    model = Article
    template_name = 'article/article_list3.html'
    context_object_name = 'articles'  # The name of the context variable in the template
    queryset = Article.objects.all().order_by('-pub_date')  # Order articles by publication date

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_message'] = 'Welcome to the article list!'
        return context


class UserArticleListView(PermissionRequiredMixin, ListView):
    """Scenario: Filter articles based on the logged-in user and pass additional context."""
    model = Article
    template_name = 'article/user_article_list.html'
    context_object_name = 'articles'
    permission_required = 'article.view_article'

    def get_queryset(self):
        """Filter articles by the logged-in user."""
        return Article.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        """Add additional context data."""
        context = super().get_context_data(**kwargs)
        context['extra_message'] = 'Articles created by you'
        return context


class PaginatedArticleListView(ListView):
    """Scenario: Paginate articles in ListView."""
    model = Article
    template_name = 'article/paginated_article_list.html'
    context_object_name = 'articles'
    paginate_by = 5  # Show 5 articles per page


class ArticleDetailView(LoggingMixin, DetailView):
    """Scenario: Add related articles (based on the same author) in the article detail view."""
    model = Article
    template_name = 'article/article_detail3.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        """Add related articles to the context."""
        context = super().get_context_data(**kwargs)
        related_articles = Article.objects.filter(
            author=self.object.author
        ).exclude(pk=self.object.pk)
        context['related_articles'] = related_articles
        return context


# class ArticleUpdateView(UpdateView):
#     """Scenario: Restrict updates to the author of the article."""
#     model = Article
#     fields = ['title', 'content']
#     template_name = 'article/article_form.html'
#     success_url = reverse_lazy('custom_article_list')

#     def dispatch(self, request, *args, **kwargs):
#         """Restrict updates to the article's author."""
#         obj = self.get_object()
#         if obj.author != self.request.user:
#             return HttpResponseForbidden("You are not allowed to edit this article.")
#         return super().dispatch(request, *args, **kwargs)

# OR WE CAN ALSO WRITE THE ABOVE CODE USING OwnerRequiredMixin MIXIN
class ArticleUpdateView(OwnerRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'articles/article_form.html'


# Combining Multiple Mixins: OwnerRequiredMixin, LoggingMixin, LoginRequiredMixin
# You can combine multiple mixins in a single view, but order matters.
# Always place mixins before the main view class in the inheritance chain.
class ArticleDeleteView(LoginRequiredMixin, LoggingMixin, OwnerRequiredMixin, DeleteView):
    """Scenario: Show a custom error if the user tries to delete someone else's article."""
    model = Article
    template_name = 'article/article_confirm_delete.html'
    success_url = reverse_lazy('custom_article_list')

    def dispatch(self, request, *args, **kwargs):
        """Restrict deletion to the article's author."""
        obj = self.get_object()
        if obj.author != self.request.user:
            return HttpResponseForbidden("You cannot delete this article.")
        return super().dispatch(request, *args, **kwargs)


# Combining CBVs with Forms (FormView)
class ContactFormView(FormView):
    """
    class ContactFormView(FormView):
    A view for displaying a contact form and handling form submission.
    """
    template_name = 'article/contact.htm'
    form_class = ContactForm
    success_url = '/article/thank-you/'

    def form_valid(self, form):
        # Add custom logic here
        form.send_email()
        return super().form_valid(form)


class ContactAuthorView(FormView):
    template_name = 'articles/contact_author.html'
    form_class = ContactAuthorForm
    success_url = reverse_lazy('custom_article_list')

    def form_valid(self, form):
        """Send a message to the article author."""
        article = Article.objects.get(pk=self.kwargs['pk'])
        message = form.cleaned_data['message']
        # Logic to send email/message to the author
        print(f"Message to {article.author}: {message}")
        return super().form_valid(form)

# class HomeRedirectView(RedirectView):
#     url = '/home/'
