from setuptools import setup, find_packages
import os

version = '1.5.2'

setup(
    name='gu.repository.content',
    version=version,
    description="Dexterity content types & behaviours for repositories.",
    long_description=open("README.txt").read() + "\n" +
                   open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Matthew Trevor',
    author_email='matthew.trevor@griffith.edu.au',
    url='http://www.griffith.edu.au',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gu', 'gu.repository'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'plone.app.dexterity [grok]',
        'plone.app.theming',
#        'plone.app.intid',
#        'plone.app.referenceablebehavior',
#        'plone.app.relationfield',
    ],
    extras_require={
        'test': ['plone.app.testing',]
    },
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
