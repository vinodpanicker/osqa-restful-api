from django.http import HttpResponseNotAllowed, HttpResponse
from django.utils.decorators import decorator_from_middleware, available_attrs
from functools import wraps

def http_basic_auth(orig_func):
    def decorator(request):
        response = HttpResponse(status=412)
        return response
    return decorator