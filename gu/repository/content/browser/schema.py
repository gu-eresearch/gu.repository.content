from zope import schema
from z3c.form import form, field
#from plone.directives import form
from gu.repository.content.interfaces import IRepositoryMetadataSchema


class SchemaEditForm(form.EditForm):

    label = u"Metadata Schema"

    #successMessage = u"Schema successfully update"
    #noChangesMessage = u"No changes were made."

    form.extends(form.EditForm)
    buttons['apply'].title = u"Save"

    @property
    def fields(self):
        fields = [
            schema.Text(
                __name__='container_schema',
                title=u'Container Schema'),
            schema.Text(
                __name__='item_schema',
                title=u'Item Schema')
        ]
        return field.Fields(*fields)
        # for f in fields.values():
        #     f.widgetFactory = SingleCheckBoxFieldWidget


    def getContent(self):
        return IRepositoryMetadataSchema(self.context)

    def applyChanges(self, data):
        val = super(SchemaEditForm, self).applyChanges(data)
        return val

