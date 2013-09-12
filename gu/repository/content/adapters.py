from zope import interface
from zope import component
from zope import annotation
from zope import location
from zope import proxy
from persistent.dict import PersistentDict
from gu.repository.content.interfaces import IRepositoryMetadataSchema
from gu.repository.content.interfaces import IRepositoryContainer

ANNO_KEY = 'gu.repository.schema'


class RepositoryMetadataSchemaAdapter(object):
    """
    This adapter looks for schema definitions attached to the repository
    container as annotations.
    """

    interface.implements(IRepositoryMetadataSchema)
    #component.adapts(annotation.IAttributeAnnotatable)

    def __init__(self, context):
        self.context = context
        self.container = None

        # walk up containment hierarchy to find first RepositoryContainer
        while getattr(context, '__parent__', None):
            if not IRepositoryContainer.providedBy(context):
                context = context.__parent__
            else:
                self.container = context
                break

    def _annotations(self):
        if self.container is None:
            return None
        annotations = annotation.interfaces.IAnnotations(self.container)
        try:
            result = annotations[ANNO_KEY]
        except KeyError:
            result = PersistentDict()
            # TODO: we know the type here and don't have to check for ILocation
            annotations[ANNO_KEY] = result
            if location.interfaces.ILocation.providedBy(result):
                location.location.locate(result,
                    proxy.removeAllProxies(self.container), ANNO_KEY)
        if not (location.interfaces.ILocation.providedBy(result)
                and result.__parent__ is context
                and result.__name__ == ANNO_KEY):
            result = location.location.LocationProxy(result, self.container, ANNO_KEY)
        return result

    def get_container_schema(self):
        anno = self._annotations()
        if anno is not None:
            return anno.get('container_schema', None)
        return None

    def set_container_schema(self, value):
        anno = self._annotations()
        if anno is not None:
            anno['container_schema'] = value
        # TODO: fail silent or noisy?

    container_schema = property(get_container_schema, set_container_schema)

    def get_item_schema(self):
        anno = self._annotations()
        if anno is not None:
            return anno.get('item_schema', None)
        return None

    def set_item_schema(self, value):
        anno = self._annotations()
        if anno is not None:
            anno['item_schema'] = value
        # TODO: fail silent or noisy?

    item_schema = property(get_item_schema, set_item_schema)
