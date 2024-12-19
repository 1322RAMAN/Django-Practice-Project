from django.urls import path
from .views import (
    register, user_login, user_logout, home, get_users,
    get_user, make_superuser, manual_login, home_view, my_view,
    check_superuser, is_staff_member, check_staff_member_required,
    staff_only_view, checking_superuser_decorator, contact
    )

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('manual_login/', manual_login, name='manual_login'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('home_view/', home_view, name='home_view'),
    path('users/', get_users, name='users'),
    path('user_details/', get_user, name='user_details'),
    path('make_superuser/', make_superuser, name='make_superuser'),
    path('my_view/', my_view, name='my_view'),
    path('check_superuser/', check_superuser, name='check_superuser'),
    path('is_staff_member/', is_staff_member, name='is_staff_member'),
    path('check_staff_member_required/', check_staff_member_required, name='check_staff_member_required'),
    path('staff_only_view/', staff_only_view, name='staff_only_view'),
    path('checking_superuser_decorator/', checking_superuser_decorator, name='checking_superuser_decorator'),
    path('contact/', contact, name='contact'),
]
