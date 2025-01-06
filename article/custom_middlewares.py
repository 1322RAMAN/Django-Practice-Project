# Middleware in Django is a way to process requests and responses globally.
import logging

logger = logging.getLogger(__name__)


# Basic Middleware Example
class CustomHeaderMiddleware:
    """A middleware that adds a custom header to all responses."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Custom-Header'] = 'My Custom Header Value-123'
        return response


# Processing Requests
class LogRequestMethodMiddleware:
    """A middleware that logs the request method."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request method: {request.method}")
        return self.get_response(request)


# Processing Responses
class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Cache-Control'] = 'no-store'
        return response


# Handling Exceptions
# Advanced Middleware Methods
# process_exception(self, request, exception)
# Executed when a view raises an exception.
class ExceptionLoggingMiddleware:
    """A middleware to log exceptions and return a custom error response."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            # Log the exception
            print(f"Exception occurred: {e}")
            # Return a custom response
            from django.http import HttpResponseServerError
            return HttpResponseServerError("A server error occurred.")
        return response

    def process_exception(self, request, exception):
        print(f"Exception: {exception}")


# Advanced Middleware Methods
# process_view(self, request, view_func, view_args, view_kwargs)
# Executed just before the view is called.
class ViewLoggingMiddleware:
    """Log the name of the view being accessed."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # This method ensures the middleware is callable
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f"View Function: {view_func.__name__}")


# process_template_response(self, request, response)
# Executed when a view returns a TemplateResponse.
class TemplateVariableMiddleware:
    """Add a variable to the template context."""
    def __init__(self, get_response):
        self.get_response = get_response

    def process_template_response(self, request, response):
        # Ensure the response has `context_data` and it is not None
        if hasattr(response, 'context_data') and response.context_data is not None:
            response.context_data['extra_variable'] = 'Extra Context Data'
        return response

    def __call__(self, request):
        # This method ensures the middleware is callable
        response = self.get_response(request)
        # Call process_template_response for TemplateResponse objects
        if hasattr(response, 'render') and callable(response.render):
            response = self.process_template_response(request, response)
        return response
