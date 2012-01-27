import os
from setuptools import setup, find_packages

version = '1.0dev'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('docs/HISTORY.txt')
    )

setup(name='collective.cmisbrowser',
      version=version,
      description="CMIS repository browser for Plone",
      long_description=long_description,
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        ],
      keywords='CMIS connection browser plone',
      author='Sylvain Viollon',
      author_email='sylvain@infrae.com',
      url='http://pypi.python.org/pypi/collective.cmisbrowser',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "setuptools",
          "plone.app.content",
          "plone.app.form",
          "suds",
          ],
      )
