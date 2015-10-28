# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import awakenlove.site


class AwakenloveSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=awakenlove.site)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'awakenlove.site:default')


AWAKENLOVE_SITE_FIXTURE = AwakenloveSiteLayer()


AWAKENLOVE_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(AWAKENLOVE_SITE_FIXTURE,),
    name='AwakenloveSiteLayer:IntegrationTesting'
)


AWAKENLOVE_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(AWAKENLOVE_SITE_FIXTURE,),
    name='AwakenloveSiteLayer:FunctionalTesting'
)


AWAKENLOVE_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        AWAKENLOVE_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='AwakenloveSiteLayer:AcceptanceTesting'
)
