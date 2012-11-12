from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from views import *

urlpatterns = patterns('',
    url(r'^%s$' % _('forum_api/user_details/'),  get_user_details, name='get_user_details'),
    url(r'^%s$' % _('forum_api/questions/'),  get_all_questions, name='get_all_questions'),    
)
