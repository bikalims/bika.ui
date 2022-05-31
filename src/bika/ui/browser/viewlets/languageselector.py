from plone.app.i18n.locales.browser.selector import LanguageSelector as Base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LanguageSelector(Base):
    template = ViewPageTemplateFile("templates/languageselector.pt")


