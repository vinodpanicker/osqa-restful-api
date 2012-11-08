from django.http import HttpResponseNotAllowed, HttpResponse
from functools import wraps
import base64
import settings

def http_basic_auth(orig_func):
    @wraps(orig_func)
    def decorator(request):    
        if request.META.has_key('HTTP_AUTHORIZATION'):
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                # NOTE: We are only support basic authentication for now.
                #
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    if uname == settings.API_USERNAME and passwd == settings.API_PASSWORD:
                        return orig_func(request)
        return HttpResponse('Unauthorized', status=401)        
    return decorator
    