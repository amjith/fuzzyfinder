#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


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
    version='1.0.0',
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
        'Development Status :: 2 - Pre-Alpha',
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
