# Author: Wei Wu <goi@shizuoka.ac.jp>
# Copyright (c) 2022 W. Wu, M. Iori, S. Martello & M Yagiura 
# License: MIT license (https://opensource.org/licenses/mit-license.php)

import setuptools

DESCRIPTION = "mmrbipy: A solver for the min-max regret binary integer programming problem (MMR-BIP)"
NAME = 'mmrbipy'
AUTHOR = 'Wei Wu'
AUTHOR_EMAIL = 'goi@shizuoka.ac.jp'
URL = 'https://github.com/ebeleta/iDS'
LICENSE = 'MIT'
VERSION = '0.1.8'
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = ['gurobipy']

with open('README.md', 'r') as fh:
    long_description = fh.read()

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    "Operating System :: OS Independent",
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Multimedia :: Graphics',
]
setuptools.setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=LICENSE,
    url=URL,
    version=VERSION,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=setuptools.find_packages(),
    classifiers=CLASSIFIERS
)