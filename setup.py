#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import ast
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('fuzzyfinder/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
        ]

test_requirements = [
    'pytest',
]

setup(
    name='fuzzyfinder',
    version=version,
    description="Fuzzy Finder implemented in Python.",
    long_description=readme + '\n\n' + history,
    author="Amjith Ramanujam",
    author_email='amjith.r@gmail.com',
    url='https://github.com/amjith/fuzzyfinder',
    packages=[
        'fuzzyfinder',
    ],
    package_dir={'fuzzyfinder':
                 'fuzzyfinder'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='fuzzyfinder',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
