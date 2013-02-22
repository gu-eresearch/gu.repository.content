from zope.interface import implements
from plone.dexterity.content import Container
from gu.repository.content.interfaces import IRepositoryItem
from plone.indexer.decorator import indexer


class RepositoryItem(Container):

    implements(IRepositoryItem)

    body = None

@indexer(IRepositoryItem)
def repositoryItem_SearchableText(object, **kw):
    return ' '.join(
        (object.title,
         object.description,
         object.body.output,
         ))
