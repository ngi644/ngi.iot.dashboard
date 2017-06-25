# encoding: utf-8

__author__ = 'nagai'


from Products.Five.browser import BrowserView
from ngi.iot.dashboard.interfaces import IDashboard
from zope.interface import implementer
from zope.interface import implements


@implementer(IDashboard)
class DashboardView(BrowserView):
    """

    """

    def __init__(self, context, request):
        super(DashboardView, self).__init__(context, request)

    def get_param(self):
        context = self.context
        sc = '''
        <script type="text/javascript">
        let app_id = '{}.mlkcca.com';
        let app_ds = '{}';
        let app_key = '{}';
        let app_pass = '{}';
        </script>
        '''.format(context.mlkcca_appid, context.mlkcca_datastore,
                   context.mlkcca_apikey, context.mlkcca_apppass)
        return sc
