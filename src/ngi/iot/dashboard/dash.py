# encoding: utf-8

__author__ = 'nagai'

from ngi.iot.dashboard.interfaces import IDashboard
from plone.dexterity.content import Item
from zope.interface import implementer


@implementer(IDashboard)
class Dashboard(Item):
    """Dashboard content class"""

