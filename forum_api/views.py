from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from decorators import http_basic_auth, require_custom_header
from forum.models import Question


@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
@require_custom_header("HTTP_USERNAME")
def get_user_details(request):
    """returns user details"""
    
    response = "not implemented yet"
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')


@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
def get_all_questions(request):
    """returns list of all questions"""

    questions = Question.objects.filter_state(deleted=False).order_by('-last_activity_at')

    #import pdb
    #pdb.set_trace()
    
    response = {}

    for q in questions:
        response[q.id] = response.get(q.id, {})
        response[q.id]['id'] = q.id
        response[q.id]['title'] = q.title
  
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
