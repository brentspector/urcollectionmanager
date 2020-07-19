# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='urcollectionmanager',
    version='1.1.3',
    description='API for Urban Rivals collection management',
    python_requires='==3.*,>=3.8.0',
    project_urls={
        "repository": "https://github.com/brentspector/urcollectionmanager"
    },
    author='Brent Spector',
    author_email='brent.spector@yahoo.com',
    license='MIT',
    packages=[],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'bs4==0.*,>=0.0.1', 'requests==2.*,>=2.23.0', 'sqlalchemy==1.*,>=1.3.15'
    ],
    extras_require={
        "dev": [
            "autopep8==1.*,>=1.5.0", "commitizen==1.*,>=1.16.4",
            "pre-commit==2.*,>=2.1.1", "pytest==5.*,>=5.3.5"
        ]
    },
)
