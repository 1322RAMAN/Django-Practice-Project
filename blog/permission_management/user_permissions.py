from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import HttpResponse
from blog.models import Blog
from user.models import CustomUser


# Assign the permission to a user
# user.user_permissions.add(permission)
# CustomUser.user_permissions.add(permission)


def check_permission(request):
    """ check permissions """
    # Get the user instance
    user = CustomUser.objects.get(email=request.user.email)

    # Get the content type for the model
    content_type = ContentType.objects.get_for_model(Blog)

    # Get or create a permission
    permission = Permission.objects.get(codename='change_blog', content_type=content_type)

    # CustomUser.user_permissions.add(permission)
    user.user_permissions.add(permission)

    # Assign custom permission (e.g., can_publish_blog)
    custom_permission = Permission.objects.get(codename="can_publish_blog")
    user.user_permissions.add(custom_permission)

    # Save the user
    user.save()

    return HttpResponse('User Permissions Added')
