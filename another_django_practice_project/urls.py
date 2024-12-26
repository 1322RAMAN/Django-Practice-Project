"""
URL configuration for another_django_practice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .default_provided_user_views import (
    home, register_user, user_login,
    create_superuser, welcome, get_user_details,
    contact_view, success, logout_user, make_superuser
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=home, name='home'),  # Root URL for the site
    path('user/', include('user.urls')),
    path('article/', include('article.urls')),
    path('generic-article/', include('article.generic_class_based_urls')),
    path('ccbv/', include('article.customized_cbv_urls')),
    path('bcbv/', include('article.basic_class_based_urls')),
    path('blog/', include('blog.urls')),
    path('register/', view=register_user, name='register_user'),
    path('login/', view=user_login, name='user_login'),
    path('create_superuser/', view=create_superuser, name='create_superuser'),
    path('welcome/', view=welcome, name='welcome'),
    path('user_details/', view=get_user_details, name='user_details'),
    path('contact/', view=contact_view, name='contact_page'),
    path('success/', view=success, name='success_page'),
    path('logout_user/', view=logout_user, name='logout_user'),
    path('make_superuser/<str:username>/', view=make_superuser, name='make_superuser'),

]
