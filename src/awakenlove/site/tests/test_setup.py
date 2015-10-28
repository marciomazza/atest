# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from awakenlove.site.testing import AWAKENLOVE_SITE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that awakenlove.site is properly installed."""

    layer = AWAKENLOVE_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if awakenlove.site is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'awakenlove.site'))

    def test_browserlayer(self):
        """Test that IAwakenloveSiteLayer is registered."""
        from awakenlove.site.interfaces import (
            IAwakenloveSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(IAwakenloveSiteLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = AWAKENLOVE_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['awakenlove.site'])

    def test_product_uninstalled(self):
        """Test if awakenlove.site is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'awakenlove.site'))

    def test_browserlayer_removed(self):
        """Test that IAwakenloveSiteLayer is removed."""
        from awakenlove.site.interfaces import IAwakenloveSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(IAwakenloveSiteLayer, utils.registered_layers())
