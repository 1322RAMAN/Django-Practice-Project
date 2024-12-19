from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from .models import Blog
from .forms import BlogForm


# When you define a model, Django automatically generates CRUD (Create, Read, Update, Delete) permissions for it.
# For Blog, these permissions will be:
# blog.add_blog
# blog.change_blog
# blog.delete_blog
# blog.view_blog


@login_required
def create_blog(request):
    """ Method for creating Blog """
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


@login_required
def blog_list(request):
    """ Method for listing Blogs """
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


@login_required
def blog_detail(request, id):
    """ Method for Blog Details """
    blog = get_object_or_404(Blog, id=id)
    if not blog:
        return HttpResponse('Blog not Found')

    # Check user permission in the view
    can_edit = request.user.has_perm("blog.change_blog")

    return render(request, 'blog/blog_detail.html', {'blog': blog, 'can_edit': can_edit})


def user_permissions(request):
    msg = []
    if request.user.has_perm('blog.change_blog'):
        print("User can change blog")
        msg.append(' User can change blog')
    if request.user.has_perm('blog.add_blog'):
        print("User can add_blog")
        msg.append(' User can add_blog')
    if request.user.has_perm('blog.delete_blog'):
        print("User can delete_blog")
        msg.append(' User can delete_blog')
    if request.user.has_perm('blog.view_blog'):
        print("User can view_blog")
        msg.append(' User can view_blog')
    else:
        print("Permission denied")
        msg.append('Permission denied')
    joined_msg = ', '.join(msg)
    return HttpResponse(joined_msg)



@login_required
@permission_required('blog.change_blog', login_url='/login/')
def edit_blog(request, blog_id):
    """
    The @permission_required decorator in Django is used to restrict access to a view based on specific user permissions.
    It ensures that only users with the required permissions can access the view.
    """
    print('----- blog_id ------', blog_id)
    blog = get_object_or_404(Blog, id=blog_id)
    # if request.method == 'POST':
    #     blog.title = request.POST.get('title')
    #     blog.content = request.POST.get('content')
    #     blog.is_published = 'is_published' in request.POST  # Checkbox handling
    #     blog.save()
    #     return redirect('blog_list')  # Replace 'blog_list' with the name of your blog list view
    # return render(request, 'edit_blog.html', {'blog': blog})
    print('------ blog -----', blog)
    return HttpResponse("You can edit this blog!")


@login_required
@permission_required('blog.delete_blog', raise_exception=True)
def delete_blog(request, blog_id):
    """
    @permission_required decorator to delete blog
    --> Raise Exception Instead of Redirecting
    """
    # View logic to delete a blog post
    blog = get_object_or_404(Blog, id=blog_id)
    # blog.delete()
    print('---- You have permissions to delete this blog ------', blog)
    return HttpResponse("Post deleted!")


@login_required
@permission_required('blog.change_blog', raise_exception=True)
@permission_required('blog.delete_blog', raise_exception=True)
def manage_blog(request, blog_id):
    """
    To require multiple permissions, use multiple decorators or logical checks within the view.
    """
    # User must have both permissions
    blog = get_object_or_404(Blog, id=blog_id)
    print('-------- User have both permissions to change or delete blog !--------', blog)
    return HttpResponse("User have both permissions to Manage post!")

