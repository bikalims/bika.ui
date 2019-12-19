from AccessControl import getSecurityManager
from OFS.ObjectManager import BeforeDeleteException
from Products.CMFCore.permissions import DeleteObjects
from Products.Five import BrowserView

bac_portal_types = [
    'Analysis',
]
bsc_portal_types = [
    'AnalysisCategory',
    'Sample',
    'SampleType',
]
pc_portal_types = [
    'AnalysisRequest',
    'Attachment',
    'Worksheet',
    'WorksheetTemplate',
    'Batch',
    'SamplePartition',
    'Sample',
    'ARImport',
    'Instrument',
    'InstrumentType',
    'Department',
    'LabContact',
]


class CleanView(BrowserView):

    def clean(self):

        context = self.context
        form = self.request.form

        # THIS IS VERY DANGEROUS!!!!!!!!!!!!!!
        # Using this script could cost you your job!
        #
        # Delete all ARs and setup data
        #
        print("Start")

        confirm = form.get('confirm', 'false').lower() == 'true'
        detail = form.get('detail', 'false').lower() == 'true'
        if not confirm:
            print("Confirm not provided - nothing will be deleted")

        sm = getSecurityManager()
        bac = context.bika_analysis_catalog
        for pt in bac_portal_types:
            brains = bac(portal_type=pt)
            print('%s = %s' % (pt, len(brains)))
            for brain in brains:
                obj = brain.getObject()
                if detail:
                    print('%s %s %s' % (pt, obj.getId(), brain.getPath()))
                if confirm:
                    try:
                        if not sm.checkPermission(DeleteObjects, obj):
                            obj.manage_permission(DeleteObjects, roles=('Manager',), acquire=0)
                        obj.aq_parent.manage_delObjects(obj.getId(),)
                    except BeforeDeleteException as e:
                        return "Failed: %s %s: %s" % (pt, obj.getId(), e)
                    except Exception as e:
                        return "Failed: %s %s: %s" % (pt, obj.getId(), e)

        bsc = context.bika_setup_catalog
        for pt in bsc_portal_types:
            brains = bsc(portal_type=pt)
            print('%s = %s' % (pt, len(brains)))
            for brain in brains:
                obj = brain.getObject()
                if detail:
                    print('%s %s %s' % (pt, obj.getId(), brain.getPath()))
                if confirm:
                    try:
                        if not sm.checkPermission(DeleteObjects, obj):
                            obj.manage_permission(DeleteObjects, roles=('Manager',), acquire=0)
                        obj.aq_parent.manage_delObjects(obj.getId(),)
                    except BeforeDeleteException as e:
                        return "Failed: %s %s: %s" % (pt, obj.getId(), e)
                    except Exception as e:
                        return "Failed: %s %s: %s" % (pt, obj.getId(), e)

        pc = context.portal_catalog
        for pt in pc_portal_types:
            brains = pc(portal_type=pt)
            print('%s = %s' % (pt, len(brains)))
            for brain in brains:
                obj = brain.getObject()
                if detail:
                    print('%s %s %s' % (pt, obj.getId(), brain.getPath()))
                if confirm:
                    try:
                        if not sm.checkPermission(DeleteObjects, obj):
                            obj.manage_permission(DeleteObjects, roles=('Manager',), acquire=0)
                        obj.aq_parent.manage_delObjects(obj.getId(),)
                    except BeforeDeleteException as e:
                        if pt == 'AnalysisRequest':
                            obj.setChildAnalysisRequest(None)
                            obj.setParentAnalysisRequest(None)
                        return "BeforeDeleteException: %s %s: %s" % (pt, obj.getId(), e)
                    except Exception as e:
                        return "Failed: %s %s: %s" % (pt, obj.getId(), e)

        print("End")
        return 'Done'
