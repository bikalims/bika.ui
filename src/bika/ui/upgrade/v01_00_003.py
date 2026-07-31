# -*- coding: utf-8 -*-

from bika.ui import PRODUCT_NAME
from bika.ui import logger
from senaite.core.upgrade import upgradestep


version = "1.0.3"
profile = "profile-senaite.core:default"


@upgradestep(PRODUCT_NAME, version)
def upgrade(tool):
    """Restore the canonical sample workflow from senaite.core."""
    portal = tool.aq_inner.aq_parent
    setup = portal.portal_setup

    setup.runImportStepFromProfile(profile, "workflow")
    logger.info("%s upgraded to version %s", PRODUCT_NAME, version)
    return True
