# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from ngi.iot.dashboard import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class INgiIotDashboardLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IDashboard(Interface):

    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    mlkcca_appid = schema.TextLine(
        title=_(u'Milkcocoa App ID'),
        required=True,
    )

    mlkcca_datastore = schema.TextLine(
        title=_(u'Milkcocoa Datastore'),
        required=True,
    )

    mlkcca_apikey = schema.TextLine(
        title=_(u'Milkcocoa API Key'),
        required=False,
    )

    mlkcca_apppass = schema.TextLine(
        title=_(u'Milkcocoa API Secret'),
        required=False,
    )
