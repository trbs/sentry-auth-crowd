#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sentry-auth-crowd
==================

:copyright: (c) 2016 Bas van Oostveen
"""

from setuptools import setup, find_packages


install_requires = [
    'sentry>=8.10.0',
    'Crowd>=1.0.1',
]

tests_require = [
    'flake8>=2.0,<2.1',
]

setup(
    name='sentry-auth-crowd',
    version='0.6.0',
    author='Bas van Oostveen',
    author_email='trbs@trbs.net',
    url='https://github.com/trbs/sentry-auth-crowd',
    description='Crowd authentication provider for Sentry',
    long_description=__doc__,
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,
    # entry_points={
    #     'sentry.apps': [
    #         'auth_crowd = sentry_auth_crowd',
    #     ],
    # },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
