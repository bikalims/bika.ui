import os

from plone.memoize.instance import memoize
from senaite.api import get_portal_type
from senaite.api import get_title
from senaite.api import get_tool
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
        print('asdf')
        title = get_title(self.context)
        name = os.path.basename(icon)
        portal_url = self.portal_state.portal_url()
        path = '{}/++plone++bika.ui.static/assets/icons'.format(portal_url)
        url = '{}/{}.png'.format(path, name)
        tag = "<img title='{}' src='{}' width='24' class='' />".format(
            title, url)
        return tag
