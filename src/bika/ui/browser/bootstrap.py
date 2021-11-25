import os

from bika.lims import api
from plone.memoize.ram import cache
from senaite.core.browser.bootstrap.bootstrap import BootstrapView as BSV
from senaite.core.browser.bootstrap.bootstrap import icon_cache_key


class BootstrapView(BSV):

    @cache(icon_cache_key)
    def get_icon_for(self, brain_or_object, **kw):
        portal_types = api.get_tool("portal_types")
        fti = portal_types.getTypeInfo(api.get_portal_type(brain_or_object))
        icon = fti and fti.getIcon()  # handle non-type fti for bbb
        if not icon:
            return ""
        title = api.get_title(brain_or_object)
        # Always try to get the SVG icon for high-res displays
        icon_basename = os.path.basename(icon)
        path = '{}/++resource++bika.lims.images/{}.png'.format(
            self.portal_state.portal_url(), icon_basename)
        # self.img_tag(title=title, icon=icon_svg, **kw)
        tag = "<img title='{}' src='{}' width='16' class='' />".format(
            title, path)
        return tag
