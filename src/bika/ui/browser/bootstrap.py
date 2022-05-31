from os.path import basename
from os.path import splitext

from bika.ui.setuphandlers import is_installed
from senaite.api import get_portal_type
from senaite.api import get_title
from senaite.api import get_tool
from senaite.core.browser.bootstrap import bootstrap
from zope.interface import implementer

PATH = "++plone++bika.ui.static/assets/icons"

WIDTH = "24px"


@implementer(bootstrap.IBootstrapView)
class BootstrapView(bootstrap.BootstrapView):

    def get_icon_for(self, brain_or_object, **kw):

        if not is_installed():
            # default from core
            return super(BootstrapView, self).get_icon_for(
                brain_or_object, **kw)

        kw['width'] = WIDTH
        portal_types = get_tool("portal_types")
        fti = portal_types.getTypeInfo(get_portal_type(brain_or_object))
        icon = fti and fti.getIcon()
        if not icon:
            return ""
        title = get_title(brain_or_object)
        icon_basename = splitext(basename(icon))[0]

        # bika.ui icon png
        icon_fn = "{}/{}.png".format(PATH, icon_basename)
        if self.resource_exists(icon_fn):
            return self.img_tag(title=title, icon=icon_fn, **kw)

        # default from core
        return super(BootstrapView, self).get_icon_for(brain_or_object, **kw)
