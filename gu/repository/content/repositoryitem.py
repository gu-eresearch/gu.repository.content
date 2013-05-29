from zope.interface import implements
from plone.dexterity.content import Container
from gu.repository.content.interfaces import IRepositoryItem
from plone.indexer.decorator import indexer
from plone.locking.interfaces import ITTWLockable


class RepositoryItem(Container):

    implements(IRepositoryItem, ITTWLockable)

    body = None

@indexer(IRepositoryItem)
def repositoryItem_SearchableText(object, **kw):
    return ' '.join(
        (object.title,
         object.description,
         object.body.output,
         ))
