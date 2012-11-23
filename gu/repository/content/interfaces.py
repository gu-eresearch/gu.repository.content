from zope import interface
from zope import schema

#

class IRepositoryContainer(interface.Interface):

    pass

class IRepositoryItem(interface.Interface):
    pass


class IRepositoryMetadata(interface.Interface):
    pass


class IRepositoryMetadataSchema(interface.Interface):

    container_schema = interface.Attribute("""raw schema representation for the container""")

    item_schema = interface.Attribute("""raw schema representation for items""")

