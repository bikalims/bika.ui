from bika.lims import bikaMessageFactory as _
from bika.lims.utils import get_image
from bika.ui.setuphandlers import is_installed
from senaite.app.listing.interfaces import IListingViewAdapter
from zope.interface import implementer


@implementer(IListingViewAdapter)
class SpecificationWarningAdapter(object):
    """Replace the shoulder warning rendered in the Result column."""

    def __init__(self, listing, context):
        self.enabled = is_installed()

    def before_render(self):
        pass

    def folder_item(self, obj, item, index):
        if not self.enabled:
            return

        after = item.get("after", {})
        result = after.get("Result", "")
        if not result:
            return

        title = _("Result in shoulder range")
        warning = get_image("warning.png", title=title)
        if warning in result:
            replacement = get_image("specification-warning.png", title=title)
            after["Result"] = result.replace(warning, replacement, 1)
