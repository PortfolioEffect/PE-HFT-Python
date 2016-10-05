"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
"""

# Always prefer setuptools over distutils
from codecs import open
from os import path
from setuptools import setup, find_packages


# To use a consistent encoding
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hft',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='High Frequency Portfolio Analytics by PortfolioEffect',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/PortfolioEffect/PortfolioEffectHFT-Python',
    download_url = 'https://github.com/PortfolioEffect/PortfolioEffectHFT-Python/tarball/1.0.0',

    # Author details
    author='Aleksey Zemnitskiy, Stephanie Toper, Andrey Kostin',
    author_email='aleksey.zemnitskiy@portfolioeffect.com, stephanie.toper@portfolioeffect.com, andrey.kostin@portfolioeffect.com',

    # Choose your license
    license='GPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords=['hft', 'trading', 'backtest', 'risk', 'microstructure'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['hft'],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['pyjnius', 'matplotlib', 'numpy', 'datetime', 'pytz', 'configparser'],
    
    package_data={'hft': ['jar/*', '*.json'] },
)