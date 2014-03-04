#import unittest2 as unittest
import unittest

from plone.app.testing import TEST_USER_NAME, TEST_USER_ID
from plone.app.testing import login, setRoles
#from plone.app.testing import logout

from gu.repository.content.tests.layer import REPOSITORYCONTENT_INTEGRAL_TESTING
from Products.CMFCore.utils import getToolByName


class SetupTest(unittest.TestCase):

    layer = REPOSITORYCONTENT_INTEGRAL_TESTING

    def test_quickinstalls(self):
        portal = self.layer['portal']

        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('gu.repository.content'))

    def test_ftis(self):
        portal = self.layer['portal']

        typesTool = getToolByName(portal, 'portal_types')
        self.assertNotEqual(typesTool.getTypeInfo('gu.repository.content.RepositoryContainer'), None)
        self.assertNotEqual(typesTool.getTypeInfo('gu.repository.content.RepositoryItem'), None)

        # TODO: get rid of stuff below
        # alternative way to do the above?
        login(portal, TEST_USER_NAME)
        setRoles(portal, TEST_USER_ID, ['Manager'])
        self.assertTrue('gu.repository.content.RepositoryContainer' in portal.portal_types)
        setRoles(portal, TEST_USER_ID, ['Member'])

    def test_roles(self):
        portal = self.layer['portal']
        # rolemap.xml
        # verify new role has been added
        self.assertTrue('Repository Administrator' in portal.valid_roles())
        # verify permissions have been assigned
        roles = [r['name'] for r in portal.rolesOfPermission('gu.repository.content: Add Repository Container') if r['selected']]
        self.assertEqual(roles, ['Manager', 'Repository Administrator'])
        roles = [r['name'] for r in portal.rolesOfPermission('gu.repository.content: Add Repository Item') if r['selected']]
        self.assertEqual(roles, ['Manager', 'Repository Administrator', 'Repository Contributor'])

    # def test_registry(self):
    #     portal = self.layer['portal']
    #     jsRegistry = getToolByName(portal, 'portal_javascripts')

    #     self.assertTrue('myscript.js' in jsRegistry.getResourceIds())
