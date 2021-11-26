import os

from bika.ui.setuphandlers import is_installed
from plone.resource.interfaces import IResourceDirectory
from senaite.core.browser.globals.interfaces import IIconProvider
from senaite.core.browser.globals.interfaces import ISenaiteTheme
from zope.component import adapts
from zope.component import getUtility
from zope.interface import implementer


@implementer(IIconProvider)
class IconProvider(object):
    adapts(ISenaiteTheme)

    priority_order = 1010

    def __init__(self, view, context):
        self.view = view
        self.context = context

    def icons(self):
        icons = {}

        if not is_installed():
            return icons

        static = getUtility(IResourceDirectory, name=u"++plone++bika.ui.static")
        for package in ("senaite.core", "senaite.patient"):
            for icon in static["assets"]["icons"][package].listDirectory():
                name, ext = os.path.splitext(icon)
                this_icon = "{}/{}/{}".format(
                    "++plone++bika.ui.static/assets/icons", package, icon)
                icons[name] = this_icon
                icons[icon] = this_icon
                # senaite will prefer existing svg, but it will be ignored
                # if it doesn't exist
                icons['%s.svg' % name] = "does-not-exist"

        return icons
