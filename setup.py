#!/usr/bin/env python

from distutils.core import setup

setup(
    name='filekeep-server',
    version='0.0.0',
    author='Gonçalo Baltazar',
    author_email='hello@goncalomb.com',
    packages=['filekeep.server'],
    install_requires=[
        'flask',
    ]
)
