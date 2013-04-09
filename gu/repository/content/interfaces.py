from zope import interface
from zope import schema
from plone.app.textfield import RichText
from plone.namedfile import field

#

class IRepositoryContainer(interface.Interface):

    body = RichText(
        title=u"Body text",
        required=False,
    #default_mime_type='text/x-rst',
    #output_mime_type='text/x-html',
    #allowed_mime_types=('text/x-rst', 'text/structured',),
    #    default=defaultBody,
    )

    logo = field.NamedBlobImage(
        title=u"Logo",
        required=False,
        )



class IRepositoryItem(interface.Interface):

    body = RichText(
        title=u"Body text",
        required=False,
    #default_mime_type='text/x-rst',
    #output_mime_type='text/x-html',
    #allowed_mime_types=('text/x-rst', 'text/structured',),
    #    default=defaultBody,
    )

    logo = field.NamedBlobImage(
        title=u"Logo",
        required=False,
        )



class IRepositoryMetadata(interface.Interface):
    pass


class IRepositoryMetadataSchema(interface.Interface):

    container_schema = interface.Attribute("""raw schema representation for the container""")

    item_schema = interface.Attribute("""raw schema representation for items""")

