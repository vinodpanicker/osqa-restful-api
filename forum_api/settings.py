from forum.settings.base import Setting, SettingSet
from django.utils.translation import ugettext_lazy as _

LDAPS_SET = SettingSet('ldaps', _('LDAPS settings'), _("LDAPS configuration for OSQA"), 4)

LDAPS_SERVER = Setting('LDAPS_SERVER', '', LDAPS_SET, dict(
label = _("LDAPs Server"),
help_text = _("The hostname of your organization's LDAP server"),
required = False))

