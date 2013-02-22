from zope.interface import implements
from plone.dexterity.content import Container
from gu.repository.content.interfaces import IRepositoryContainer
from plone.indexer.decorator import indexer

class RepositoryContainer(Container):

    implements(IRepositoryContainer)

    body = None


@indexer(IRepositoryContainer)
def repositoryContainer_SearchableText(object, **kw):
    return ' '.join(
        (object.title,
         object.description,
         object.body.output,
         ))
