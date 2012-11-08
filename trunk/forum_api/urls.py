from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from views import get_questions

urlpatterns = patterns('',
    url(r'^%s$' % _('forum_api/questions/'),  get_questions, name='get_questions'),
)
