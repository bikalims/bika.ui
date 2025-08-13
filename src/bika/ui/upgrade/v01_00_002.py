# -*- coding: utf-8 -*-

from bika.ui import PRODUCT_NAME
from bika.ui import PROFILE_ID
from bika.ui import logger
from senaite.core.upgrade import upgradestep
from senaite.core.upgrade.utils import UpgradeUtils

version = "1.0.2"


@upgradestep(PRODUCT_NAME, version)
def upgrade(tool):
    portal = tool.aq_inner.aq_parent
    setup = portal.portal_setup
    portal = tool.aq_inner.aq_parent
    ut = UpgradeUtils(portal)
    ver_from = ut.getInstalledVersion(PRODUCT_NAME)

    if ut.isOlderVersion(PRODUCT_NAME, version):
        logger.info("Skipping upgrade of {0}: {1} > {2}".format(
            PRODUCT_NAME, ver_from, version))
        return True

    # -------- ADD YOUR STUFF BELOW --------

    setup.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")
    logger.info("{0} upgraded to version {1}".format(PRODUCT_NAME, version))
    return True
