# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
import os
from setuptools import setup

BASEDIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASEDIR, 'README.rst'), 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='mathml2omml',
    version='0.0.1',
    description='',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/amedama41/mathml2omml',
    author='amedama41',
    author_email='kamo.devel41@gmail.com',
    keywords=['MathML', 'OpenXML'],
    packages=['mathml2omml'],
    install_requires=[],
    python_requires='>=3.5',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Markup :: XML',
    ]
)
