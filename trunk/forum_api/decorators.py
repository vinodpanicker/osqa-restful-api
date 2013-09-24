from django.http import HttpResponseNotAllowed, HttpResponse
from functools import wraps
import base64
import settings

from forum.models import User

def http_basic_auth(orig_func):
    """
    This is decorator checking if request has HTTP_AUTHORIZATION 
    header set and are auth data correct.
    """
    @wraps(orig_func)
    def decorator(request, *args, **kwargs):    
        if request.META.has_key('HTTP_AUTHORIZATION'):
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                # NOTE: We are only support basic authentication for now.
                #
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1]).split(':')
                    if uname == settings.API_USERNAME and passwd == settings.API_PASSWORD:
                        return orig_func(request, *args, **kwargs)
        return HttpResponse('Unauthorized', status=401)        
    return decorator
    

def require_custom_header(custom_header_name):
    """
    This is decorator checking if request has correct custom header defined.
    """
    def decorator(orig_func):
        def wrapper(request, *args, **kwargs):
            
            def custom_header(orig_func, request, 
                                custom_header_name, *args, **kwargs):

                if request.POST.has_key(custom_header_name):
                    username = request.POST[custom_header_name].split()
                    if len(username) == 1:
                        return orig_func(request, *args, **kwargs)
                return HttpResponse('Missing %s header' % custom_header_name, status=400)
            
            return custom_header(orig_func, request, 
                                 custom_header_name, *args, **kwargs)
        return wrapper        
    return decorator;

def require_ask_questions_header(custom_header_name):
    """
    This is decorator checking if request has ask questions headers defined.
    """
    def decorator(orig_func):
        def wrapper(request, *args, **kwargs):
            
            def custom_header(orig_func, request, 
                                custom_header_name, *args, **kwargs):

                if request.POST.has_key(custom_header_name):
                    return orig_func(request, *args, **kwargs)
                return HttpResponse('Missing %s header' % custom_header_name, status=400)
            
            return custom_header(orig_func, request, 
                                 custom_header_name, *args, **kwargs)
        return wrapper        
    return decorator;

    

def check_user_exists(orig_func):
    """
    This is decorator checking if requested user name exists in database.
    """
    @wraps(orig_func)
    def decorator(request, *args, **kwargs):
        
        user_name = request.POST['USERNAME']
        
        try:
            user = User.objects.get(username__iexact=user_name)
        except:
            return HttpResponse('User %s not found' % user_name, status=400)
        
        return orig_func(request, *args, **kwargs)        
     
    return decorator
