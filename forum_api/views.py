from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from forum.models import Question, User

from decorators import *
from utils import *


@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
@require_custom_header("HTTP_USERNAME")
@check_user_exists
def get_user_details(request):
    """returns requested user details"""
    
    requested_user = []
    
    user_name = request.META['HTTP_USERNAME']    
    requested_user.append(User.objects.get(username__iexact=user_name))
    response = user_list(requested_user)    

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
   

@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
def get_all_questions(request):
    """returns list of all questions sorted by last activity date"""

    questions = Question.objects.filter_state(deleted=False).order_by('-last_activity_at')
    response = question_list(questions)

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
