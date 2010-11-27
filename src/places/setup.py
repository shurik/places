from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='places',
      version=version,
      description="A Django project for a Maps and Facebook art project",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Aleksandr Vladimirskiy',
      author_email='sasha@theotheralex.com',
      url='http://theotheralex.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
