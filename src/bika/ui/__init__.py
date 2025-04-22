# -*- coding: utf-8 -*-
#
# This file is part of BIKA.UI
#
# Copyright 2019 by it's authors.

import logging
from zope.i18nmessageid import MessageFactory

from bika.lims.api import get_request
from bika.ui.interfaces import IBikaUILayer

PRODUCT_NAME = "bika.ui"
PROFILE_ID = "profile-{}:default".format(PRODUCT_NAME)
logger = logging.getLogger(PRODUCT_NAME)
_ = MessageFactory(PRODUCT_NAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    logger.info("*** Initializing BIKA.UI ***")


def is_installed():
    """Returns whether the product is installed or not"""
    request = get_request()
    return IBikaUILayer.providedBy(request)
