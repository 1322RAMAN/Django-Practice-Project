from django.utils.timezone import now
from django.http import HttpResponseForbidden


class LoggingMixin:
    """Logs every request to the console."""
    def dispatch(self, request, *args, **kwargs):
        print(f"Logging = [{now()}] {request.method} request at {request.path}")
        return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin:
    """Restricts access to views to the object's owner."""
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden("You are not the owner of this object.")
        return super().dispatch(request, *args, **kwargs)
