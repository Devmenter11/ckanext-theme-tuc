# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='''ckanext-theme-tuc''',

    version='0.0.1',

    description='''CKAN Theme Technische Universität Chemnitz''',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://gitlab.hrz.tu-chemnitz.de/flwer--tu-chemnitz.de/ckanext-theme-tuc',

    author='''Florian Werner''',
    author_email='''flwer@hrz.tu-chemnitz.de''',

    license='AGPL',

    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],


    keywords='''CKAN''',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        namespace_packages=['ckanext'],

    install_requires=[
      # CKAN extensions should not list dependencies here, but in a separate
      # ``requirements.txt`` file.
    ],

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    include_package_data=True,
    package_data={
    },

    data_files=[],

    entry_points='''
        [ckan.plugins]
        theme_tuc=ckanext.theme_tuc.plugin:ThemeTucPlugin

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',

    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
