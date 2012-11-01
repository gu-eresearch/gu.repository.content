# to grok stuff use this as base: dexterity.DisplayForm, dexterity.EditForm
#from plone.directives import dexterity

# not grokking? .. use these: edit.DefaultEditForm view.DefaulView
from plone.dexterity.browser import edit, view
from plone.supermodel import loadString
from gu.repository.content.interfaces import IRepositoryMetadata

SCHEMA = """<?xml version="1.0"?>
<model xmlns="http://namespaces.plone.org/supermodel/schema">
  <!-- Schema for the animal type -->
  <schema>
    <field name="species" type="zope.schema.TextLine">
      <description />
      <title>Species</title>
    </field>
    <field name="feeding_notes" type="plone.app.textfield.RichText">
      <description />
      <title>Feeding Notes</title>
    </field>
    <!-- pre Plone 4.3 needs z3c.blobfile for this to work -->
    <field name="passport_photo" type="plone.namedfile.field.NamedBlobImage">
      <description />
      <title>Passport Photo</title>
    </field>
  </schema>
</model>
"""

class MetadataView(view.DefaultView):

    id = 'view_metadata'
    enctype = 'text/html'

    @property
    def schema(self):
        model = loadString(SCHEMA)
        return model.schemata[""]

    @property
    def additionalSchemata(self):
        model = loadString(SCHEMA)
        # return only those schemata, where k is set
        return [s for k, s in model.schemata.items() if k]

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


class MetadataEdit(edit.DefaultEditForm):

    @property
    def schema(self):
        model = loadString(SCHEMA)
        return model.schemata[""]

    @property
    def additionalSchemata(self):
        model = loadString(SCHEMA)
        # return only those schemata, where k is set
        return [s for k, s in model.schemata.items() if k]

    def getContent(self):
        return IRepositoryMetadata(self.context)
