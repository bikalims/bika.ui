import os

from plone.memoize.instance import memoize
from bika.lims.api import get_portal_type
from bika.lims.api import get_title
from bika.lims.api import get_tool
from senaite.core.browser.viewlets import listings


class ListingTableTitleViewlet(listings.ListingTableTitleViewlet):
    """This viewlet inserts the title and context actions
    """

    @property
    @memoize
    def icon(self):
        portal_types = get_tool("portal_types")
        fti = portal_types.getTypeInfo(get_portal_type(self.context))
        icon = fti and fti.getIcon()  # handle non-type fti for bbb
        if not icon:
            return ""
        title = get_title(self.context)
        name = os.path.basename(icon)
        path_prefix = "{}/++plone++bika.ui.static/assets/icons"

        if name == "sample" or name == "batch":
            qi = get_tool("portal_quickinstaller")
            if qi.isProductInstalled("senaite.patient"):
                path_prefix = "{}/++plone++bika.ui.static/assets/patient"

        portal_url = self.portal_state.portal_url()
        path = path_prefix.format(portal_url)
        url = '{}/{}.png'.format(path, name)
        tag = "<img title='{}' src='{}' width='24' class='' />".format(
            title, url)
        return tag
