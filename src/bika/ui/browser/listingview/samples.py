# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from bika.ui import _
from bika.ui import is_installed
from senaite.app.listing.interfaces import IListingView
from senaite.app.listing.interfaces import IListingViewAdapter


class SamplesListingViewAdapter(object):
    adapts(IListingView)
    implements(IListingViewAdapter)

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
        if not is_installed():
            return

        import pdb; pdb.set_trace()
        for i in self.listing.review_states:
            if i["title"] == "Dispatched":
                i["title"] = _("Disposed")

    def folder_item(self, obj, item, index):
        if not is_installed():
            return item
        return item
