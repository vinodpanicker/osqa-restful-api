from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from lib.decorators import http_basic_auth

@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
def get_questions(request):

    #import pdb
    #pdb.set_trace()

    questions = {
        "key1": "value1",
        "key2": "value2"
    }
    
    return HttpResponse(simplejson.dumps(questions), mimetype='application/json')
