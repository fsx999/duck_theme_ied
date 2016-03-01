
from django.template import loader
from django.utils.text import capfirst
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext as _

from xadmin.sites import site
from xadmin.filters import SEARCH_VAR
from xadmin.views import BaseAdminPlugin, CommAdminView
import copy

class IEDPlugin(BaseAdminPlugin):
    urls = [
        {'name': 'Wiki', 'url': '/wiki'},
        # {'name': 'Forum', 'url': '/forum'},
        {'name': 'Support', 'url': '/support'},
    ]

    def get_context(self, context):
        return context

    # Block Views
    def block_top_navbar(self, context, nodes):
        urls = copy.deepcopy(self.urls)
        if self.request.user.is_superuser:
            urls.append({'name': 'Admin', 'url': '/admin'})
        nodes.append(
            loader.render_to_string('xadmin_plugins/comm.top.lien.html', {'urls': urls}))

