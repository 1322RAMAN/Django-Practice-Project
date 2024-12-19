from django.db import models
from django.urls import reverse
from user.models import CustomUser


class Blog(models.Model):
    """
    Blog Model
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the CustomUser model
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto timestamp on every save
    is_published = models.BooleanField(default=False)  # Publish status

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return reverse('blog_detail', args=[self.id])

    class Meta:
        """ You can define your own permissions in the model's Meta class. """
        permissions = [
            ("publish_blog", "Can publish blog"),
            ("archive_blog", "Can archive blog"),
        ]
