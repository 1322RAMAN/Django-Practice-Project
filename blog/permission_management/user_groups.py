from django.contrib.auth.models import Group, Permission
from django.shortcuts import HttpResponse
from user.models import CustomUser


# Groups allow you to assign permissions to multiple users at once. A user can belong to multiple groups.
def user_group(request):
    """ Create a new group, Add permissions to the group and Add user to group. """
    # Create a new group
    editors_group, created = Group.objects.get_or_create(name="Editors")

    # Add permissions to the group
    permission = Permission.objects.get(codename="change_blog")
    editors_group.permissions.add(permission)
    editors_group.save()

    # get custom user
    user = CustomUser.objects.get(email=request.user.email)

    # Add user to group
    user.groups.add(editors_group)
    user.save()
    return HttpResponse('User Groups')


def check_user_group(request):
    """ Checking Group Membership """
    # get custom user
    user = CustomUser.objects.get(email=request.user.email)

    if user.groups.filter(name="Editors").exists():
        print("User is an editor")
        msg = "User is an editor"
    else:
        print("User is not an editor")
        msg = "User is not an editor"
    return HttpResponse(msg)
