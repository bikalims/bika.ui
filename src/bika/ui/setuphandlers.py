from bika.ui import PROFILE_ID
from bika.ui import logger
from bika.ui.interfaces import IBikaUILayer
from plone.api.portal import set_registry_record
from senaite.api import get_request
from senaite.core.setuphandlers import _run_import_step


def is_installed():
    request = get_request()
    return IBikaUILayer.providedBy(request)


def install(context):
    if context.readDataFile("bika.ui.default.txt") is None:
        return
    logger.info("BIKA.UI install handler [BEGIN]")
    portal = context.getSite()
    _run_import_step(portal, "skins", PROFILE_ID)
    _run_import_step(portal, "browserlayer", PROFILE_ID)
    logger.info("BIKA.UI install handler [DONE]")


def post_install(portal_setup):
    pass


def uninstall(context):
    if context.readDataFile("bika.ui.uninstall.txt") is None:
        return
    portal = context.getSite()
    reset_settings(portal)


def reset_settings(portal):
    """Reset the settings from registry to match with defaults
    """
    logger.info("BIKA.UI Reset core registry defaults")
    root = "/++plone++senaite.core.static"
    default_settings = {
        "plone.site_title": u"SENAITE LIMS",
        "senaite.toolbar_logo": u"{}/images/senaite.svg".format(root),
        "senaite.toolbar_logo_styles": {"height": "15px"},
    }

    for key, val in default_settings.items():
        set_registry_record(key, val)

    logger.info("BIKA.UI Reset core registry defaults [DONE]")
