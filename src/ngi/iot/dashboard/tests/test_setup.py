# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ngi.iot.dashboard.testing import NGI_IOT_DASHBOARD_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ngi.iot.dashboard is properly installed."""

    layer = NGI_IOT_DASHBOARD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ngi.iot.dashboard is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ngi.iot.dashboard'))

    def test_browserlayer(self):
        """Test that INgiIotDashboardLayer is registered."""
        from ngi.iot.dashboard.interfaces import (
            INgiIotDashboardLayer)
        from plone.browserlayer import utils
        self.assertIn(INgiIotDashboardLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NGI_IOT_DASHBOARD_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ngi.iot.dashboard'])

    def test_product_uninstalled(self):
        """Test if ngi.iot.dashboard is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ngi.iot.dashboard'))

    def test_browserlayer_removed(self):
        """Test that INgiIotDashboardLayer is removed."""
        from ngi.iot.dashboard.interfaces import \
            INgiIotDashboardLayer
        from plone.browserlayer import utils
        self.assertNotIn(INgiIotDashboardLayer, utils.registered_layers())
