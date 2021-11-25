from bika.ui import PRODUCT_NAME
from bika.ui import PROFILE_ID
from bika.ui import logger
from bika.ui.interfaces import IBikaUILayer
from senaite.api import get_request


def is_installed():
    request = get_request()
    return IBikaUILayer.providedBy(request)


def post_install(portal_setup):
    """Runs after the last import step of the *default* profile
    This handler is registered as a *post_handler* in the generic setup profile
    :param portal_setup: SetupTool
    """
    logger.info("{} post-install handler [BEGIN]".format(PRODUCT_NAME.upper()))
    context = portal_setup._getImportContext(PROFILE_ID)
    portal = context.getSite()  # noqa

    logger.info("{} post-install handler [DONE]".format(PRODUCT_NAME.upper()))
