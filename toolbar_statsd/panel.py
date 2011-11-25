from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _, ungettext
from django.contrib.humanize.templatetags.humanize import intcomma
from debug_toolbar.panels import DebugPanel

from statsd.client import StatsClient


class StatsClient(StatsClient):

    def reset(self):
        self.cache = []

    def _send(self, stat, value, rate):
        num, scale = value.split('|')
        value = '%s%s' % (intcomma(int(num)), scale)
        self.cache.append([stat, value, rate])


class StatsdPanel(DebugPanel):

    name = 'Statsd'
    has_content = True

    def __init__(self, *args, **kw):
        super(StatsdPanel, self).__init__(*args, **kw)
        from statsd import statsd
        self.statsd = statsd
        self.statsd.reset()

    def nav_title(self):
        return _('Statsd')

    def nav_subtitle(self):
        length = len(self.statsd.cache)
        return ungettext('%s record', '%s records', length) % length

    def title(self):
        return _('Statsd')

    def url(self):
        return ''

    def content(self):
        context = self.context.copy()
        context.update(settings.TOOLBAR_STATSD)
        context['statsd'] = self.statsd.cache
        return render_to_string('toolbar_statsd/statsd.html', context)


