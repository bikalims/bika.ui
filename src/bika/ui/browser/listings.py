# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.CORE.
#
# SENAITE.CORE is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2021 by it's authors.
# Some rights reserved, see README and LICENSE.

import os
from bika.lims import api
from plone.memoize.instance import memoize
from senaite.core.browser.viewlets.listings import ListingTableTitleViewlet as LTTV


class ListingTableTitleViewlet(LTTV):

    @property
    @memoize
    def icon(self):
        portal_types = api.get_tool("portal_types")
        fti = portal_types.getTypeInfo(api.get_portal_type(self.context))
        icon = fti and fti.getIcon()  # handle non-type fti for bbb
        if not icon:
            return ""
        title = api.get_title(self.context)
        # Always try to get the SVG icon for high-res displays
        icon_basename = os.path.basename(icon)
        # if '_big' in icon_basename:
        #     import pdb; pdb.set_trace()
        path = '{}/++resource++bika.lims.images/{}.png'.format(self.portal_state.portal_url(), icon_basename)
        # self.img_tag(title=title, icon=icon_svg, **kw)
        tag = "<img title='{}' src='{}' width='16' class='' />".format(title, path)
        return tag
