from bika.lims.interfaces import IBikaLIMS
from senaite.lims.interfaces import ISenaiteLIMS


class IBikaUILayer(IBikaLIMS, ISenaiteLIMS):
    """Marker interface that defines a Zope 3 browser layer.
    """
