# to grok stuff use this as base: dexterity.DisplayForm, dexterity.EditForm
#from plone.directives import dexterity

# not grokking? .. use these: edit.DefaultEditForm view.DefaulView
from plone.dexterity.browser import edit, view
from plone.supermodel import loadString
from gu.repository.content.interfaces import IRepositoryMetadata, IRepositoryMetadataSchema
from gu.repository.content.interfaces import IRepositoryContainer, IRepositoryItem

# <?xml version="1.0"?>
# <model xmlns="http://namespaces.plone.org/supermodel/schema">
#   <schema>
#     <field name="species" type="zope.schema.TextLine">
#       <description />
#       <title>Species</title>
#     </field>
#     <field name="feeding_notes" type="plone.app.textfield.RichText">
#       <description />
#       <title>Feeding Notes</title>
#     </field>
#     <!-- pre Plone 4.3 needs z3c.blobfile for this to work -->
#     <field name="passport_photo" type="plone.namedfile.field.NamedBlobImage">
#       <description />
#       <title>Passport Photo</title>
#     </field>
#   </schema>
# </model>


class ModelMixin(object):

    _model = None

    @property
    def model(self):
        if self._model is None:
            self._model = self._load_model()
        return self._model

    def _load_model(self):
        if self._model is None:
            schemaAdapter = IRepositoryMetadataSchema(self.context)
            if IRepositoryContainer.providedBy(self.context):
                self._model = loadString(schemaAdapter.container_schema)
            elif IRepositoryItem.providedBy(self.context):
                self._model = loadString(schemaAdapter.item_schema)
        return self._model


class MetadataView(ModelMixin, view.DefaultView):

    id = 'view_metadata'
    enctype = 'text/html'

    def update(self):
        super(MetadataView, self).update()

    @property
    def schema(self):
        return self.model.schemata[""]
        
    @property
    def additionalSchemata(self):
        # return only those schemata, where k is set (exclude default schema returned by self.schema)
        return [s for k, s in self.model.schemata.items() if k]

    def getContent(self):
        return IRepositoryMetadata(self.context)

    def updateWidgets(self):
        super(MetadataView, self).updateWidgets()

    def render(self):
        '''See interfaces.IForm'''
        # render content template
        import zope.component
        from zope.pagetemplate.interfaces import IPageTemplate

        if self.template is None:
            template = zope.component.getMultiAdapter((self, self.request),
                IPageTemplate)
            return template(self)
        return self.template()
        

class MetadataEdit(ModelMixin, edit.DefaultEditForm):

    def update(self):
        super(MetadataEdit, self).update()
        # plone/z3cform/fieldsets/extensible.py(57)update()
        #     self.updateFields()
        #     plone/autoform/form.py(29)updateFields()
        #         self.updateFieldsFromSchemata()
        #             starts with self.fields
        #             go through self.groups and trun them into GroupFactory
        #             look at self.schema -> do processFields with permissioncheck
        #             plone/autoform/utils.py(125)processFields()
        #                 setup fields, groups, fieldsets form given schema
        #             look at self.additionalSchemata
        #         plone/z3cform/fieldsets/extensible.py(61)updateFields()
        #             lookup IFormExtender adapters
        # -> updateWidgets
        # -> 

    @property
    def schema(self):
        return self.model.schemata[""]

    @property
    def additionalSchemata(self):
        # return only those schemata, where k is set (exclude default schema returned by self.schema)
        return [s for k, s in self.model.schemata.items() if k]

    def getContent(self):
        return IRepositoryMetadata(self.context)
