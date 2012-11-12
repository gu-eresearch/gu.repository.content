from plone.testing import z2
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import applyProfile
#from plone.app.testing improt quickInstallProduct
#quickInstallProduct(portal, productname, reinstall=False)


class RepositoryContentFixture(PloneSandboxLayer):
    """Configure gu.repository.content"""

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):

        import gu.repository.content
        self.loadZCML(package=gu.repository.content)

    def setUpPloneSite(self, portal):
        """ do special site setup here"""
        applyProfile(portal, 'gu.repository.content:default')


REPOSITORYCONTENT_FIXTURE = RepositoryContentFixture()

REPOSITORYCONTENT_INTEGRAL_TESTING = IntegrationTesting(bases=(REPOSITORYCONTENT_FIXTURE, ), name="RepositoryContentFixture:Integral")
REPOSITORYCONTENT_FUNCTIONAL_TESTING = FunctionalTesting(bases=(REPOSITORYCONTENT_FIXTURE, ), name="RepositoryContentFixture:Functional")
REPOSITORYCONTENT_ZSERVER = FunctionalTesting(bases=(REPOSITORYCONTENT_FIXTURE, z2.ZSERVER_FIXTURE), name="RepositoryContentFixture:ZServer")


# Notes: use PloneSandboxLayer and setupZope, setupPloneSite (+ tearDownXXX), to create a custom Plone site fixture


#         zcml.load_config("configure.zcml", gu.repository.content)
