from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from senaite.core.browser.viewlets import toolbar


class ToolbarViewletManager(toolbar.ToolbarViewletManager):
    custom_template = ViewPageTemplateFile("templates/toolbar.pt")
