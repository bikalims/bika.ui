from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from bika.ui.setuphandlers import is_installed
from plone.app.layout.links.viewlets import render_cachekey
from plone.app.layout.viewlets import ViewletBase
from plone.memoize import ram
from plone.memoize.compress import xhtml_compress


class LocalStylesViewlet(ViewletBase):
    _template = ViewPageTemplateFile("templates/localstyles.pt")

    @ram.cache(render_cachekey)
    def render(self):
        if is_installed():
            return xhtml_compress(self._template())
