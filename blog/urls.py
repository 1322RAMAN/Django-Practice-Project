from django.urls import path
from .views import (
    create_blog, blog_detail, blog_list,
    edit_blog, delete_blog, manage_blog,
    user_permissions
    )
from .permission_management.user_permissions import check_permission
from .permission_management.user_groups import user_group, check_user_group

urlpatterns = [
    path('create_blog/', create_blog, name='create_blog'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_detail/<int:id>/', blog_detail, name='blog_detail'),
    path('edit_blog/<int:blog_id>/', edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('manage_blog/<int:blog_id>/', manage_blog, name='manage_blog'),
    path('manage_blog/', manage_blog, name='manage_blog'),
    path('user_permissions/', user_permissions, name='user_permissions'),
    path('check_permission/', check_permission, name='check_permission'),
    path('user_group/', user_group, name='user_group'),
    path('check_user_group/', check_user_group, name='check_user_group'),
]
