# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ngi.iot.dashboard


class NgiIotDashboardLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ngi.iot.dashboard)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ngi.iot.dashboard:default')


NGI_IOT_DASHBOARD_FIXTURE = NgiIotDashboardLayer()


NGI_IOT_DASHBOARD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NGI_IOT_DASHBOARD_FIXTURE,),
    name='NgiIotDashboardLayer:IntegrationTesting'
)


NGI_IOT_DASHBOARD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NGI_IOT_DASHBOARD_FIXTURE,),
    name='NgiIotDashboardLayer:FunctionalTesting'
)


NGI_IOT_DASHBOARD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NGI_IOT_DASHBOARD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='NgiIotDashboardLayer:AcceptanceTesting'
)
