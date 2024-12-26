from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


# AbstractBaseUser ###
# Provides the core implementation for a user model:
# Includes fields like password, last_login, etc.
# Does not include fields like username, email, or is_active, which you define in CustomUser.

# PermissionsMixin ###
# Adds fields and methods for handling user permissions:
# is_superuser: Indicates if the user is a superuser.
# groups and user_permissions: Allow assigning permissions to users.


class CustomUserManager(BaseUserManager):
    """This is the custom manager for the CustomUser model. It provides methods to create both regular users and superusers."""
    def create_user(self, email, password=None, **extra_fields):
        """ Used to create regular users. """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)                 # Converts email to lowercase for consistency using normalize_email.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Used to create superusers (administrators with all permissions). """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """This is the custom user model that inherits from AbstractBaseUser and PermissionsMixin."""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()   # Links the model to the custom manager for user creation. e.g,( CustomUser.objects.create_superuser(email="admin@example.com", password="adminpassword") )

    USERNAME_FIELD = 'email'    # Specifies email as the unique identifier for authentication instead of the default username.
    REQUIRED_FIELDS = []    # Specifies fields required when creating a superuser using createsuperuser. Here, only email is mandatory.

    def __str__(self):
        """Returns the user's email as its string representation."""
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        """ You can also define custom permissions in your CustomUser or other models using the Meta class. """
        permissions = [
            ("can_publish_blog", "Can publish blog"),
        ]
