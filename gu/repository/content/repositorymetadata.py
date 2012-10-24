from zope import interface
from zope import component
from zope import annotation
from persistent.dict import PersistentDict

#

ANNO_KEY = 'gu.repository'

#

class IRepositoryMetadata(interface.Interface):
    pass

#

class RepositoryMetadata(PersistentDict):
    interface.implements(IRepositoryMetadata)
    component.adapts(annotation.IAttributeAnnotatable)

#

RepositoryMetadataAdapter = annotation.factory(RepositoryMetadata, key=ANNO_KEY)
