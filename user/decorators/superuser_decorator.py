from django.http import HttpResponseForbidden
from functools import wraps


# 5. @superuser_required (Custom Decorator)
# Django doesn't come with a built-in @superuser_required decorator, but you can create a custom one to ensure the user is a superuser.

def superuser_required(view_func):
    """ Usage: It restricts access to views to only superusers. """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized to view this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
