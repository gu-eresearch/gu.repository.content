from zope.interface import implements
from plone.dexterity.content import Container
from gu.repository.content.interfaces import IRepositoryContainer

class RepositoryContainer(Container):

    implements(IRepositoryContainer)
