import ckan.plugins as p
from ckan.lib.base import BaseController

class StatsController(BaseController):
    def stats(self):
        return p.toolkit.render('stats.html')