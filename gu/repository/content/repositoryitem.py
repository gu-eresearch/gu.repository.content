from zope.interface import implements
from plone.dexterity.content import Container
from gu.repository.content.interfaces import IRepositoryItem


class RepositoryItem(Container):

    implements(IRepositoryItem)
