from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from forum.models import Question, User, Node
from django.db import connection, transaction
from decorators import *
from utils import *


@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
@require_custom_header("USERNAME")
@check_user_exists
def get_user_details(request):
    """returns requested user details"""
    
    requested_user = []
    
    user_name = request.POST['USERNAME']    
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

@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
@require_ask_questions_header("KEYWORDS")
def search_questions(request):
    """returns questions mathching keywords"""
    keywords = request.POST['KEYWORDS']   

    questions = Question.objects.filter(title__contains=keywords)
    response = question_list(questions)

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

@require_http_methods(["POST"])
@csrf_exempt
@http_basic_auth
@require_ask_questions_header("TITLE")
@require_ask_questions_header("TAGS")
@require_ask_questions_header("AUTHORID")
@require_ask_questions_header("BODY")
def ask_questions(request):
    """sk questions API"""  
    qtitle = request.POST['TITLE']   
    tags = request.POST['TAGS']
    author = request.POST['AUTHORID']
    qbody = request.POST['BODY']
    p2 = Node(title = qtitle, tagnames = tags, author_id = author, body = qbody, node_type = "question")
    "cannot succeed in setting node_type here and I don't know why"
    p2.save()

    " change node_type to question"
    cursor = connection.cursor()
    sql = "update forum_node set node_type = 'question' where 1 order by id desc limit 1;"
    cursor.execute(sql)

    questions = Question.objects.filter(title__contains=qtitle)
    response = question_list(questions)

    return HttpResponse(simplejson.dumps(response), mimetype='application/json')







