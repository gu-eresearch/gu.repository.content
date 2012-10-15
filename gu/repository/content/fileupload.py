from five import grok
from Acquisition import aq_parent
from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.container.interfaces import INameChooser
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from collective.quickupload.portlet import quickuploadportlet
from collective.quickupload.interfaces import IQuickUploadCapable
from .interfaces import IRepositoryContainer, IRepositoryItem

FILEUPLOAD_PORTLET_COLUMN = u'plone.rightcolumn' # TODO: expose this?

@grok.subscribe(IRepositoryContainer, IObjectAddedEvent)
@grok.subscribe(IRepositoryItem, IObjectAddedEvent)
def add_fileupload_portlet(obj, event):
    if not IQuickUploadCapable(obj):
        return
    column = getUtility(IPortletManager, name=FILEUPLOAD_PORTLET_COLUMN)
    manager = getMultiAdapter((obj, column), IPortletAssignmentMapping)
    assignment = quickuploadportlet.Assignment()
    chooser = INameChooser(manager)
    manager[chooser.chooseName(None, assignment)] = assignment

