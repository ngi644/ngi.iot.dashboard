# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from ngi.iot.dashboard.interfaces import IDashboard
from ngi.iot.dashboard.testing import NGI_IOT_DASHBOARD_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class DashboardIntegrationTest(unittest.TestCase):

    layer = NGI_IOT_DASHBOARD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Dashboard')
        schema = fti.lookupSchema()
        self.assertEqual(IDashboard, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Dashboard')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Dashboard')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IDashboard.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Dashboard',
            id='Dashboard',
        )
        self.assertTrue(IDashboard.providedBy(obj))
