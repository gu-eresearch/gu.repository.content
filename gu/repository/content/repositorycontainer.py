from zope.interface import implements
from plone.dexterity.content import Container
from gu.repository.content.interfaces import IRepositoryContainer
from plone.indexer.decorator import indexer
from plone.locking.interfaces import ITTWLockable

class RepositoryContainer(Container):

    implements(IRepositoryContainer, ITTWLockable)

    body = None


@indexer(IRepositoryContainer)
def repositoryContainer_SearchableText(object, **kw):
    return ' '.join(
        (object.title,
         object.description,
         object.body.output,
         ))
