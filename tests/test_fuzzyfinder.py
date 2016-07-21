#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fuzzyfinder
----------------------------------

Tests for `fuzzyfinder` module.
"""
import pytest
from fuzzyfinder import fuzzyfinder

@pytest.fixture
def collection():
    return ['migrations.py',
            'django_migrations.py',
            'django_admin_log.py',
            'api_user.doc',
            'user_group.doc',
            'users.txt',
            'accounts.txt',
            '123.py',
            'test123test.py'
            ]

@pytest.fixture
def dict_collection():
    return [
            {'name': 'migrations.py'},
            {'name': 'django_migrations.py'},
            {'name': 'django_admin_log.py'},
            {'name': 'api_user.doc'},
            {'name': 'user_group.doc'},
            {'name': 'users.txt'},
            {'name': 'accounts.txt'},
            ]

def test_substring_match(collection):
    text = 'txt'
    results = fuzzyfinder(text, collection)
    expected = ['users.txt', 'accounts.txt']
    assert list(results) == expected

def test_substring_match_with_dot(collection):
    text = '.txt'
    results = fuzzyfinder(text, collection)
    expected = ['users.txt', 'accounts.txt']
    assert list(results) == expected

def test_fuzzy_match(collection):
    text = 'djmi'
    results = fuzzyfinder(text, collection)
    expected = ['django_migrations.py', 'django_admin_log.py']
    assert list(results) == expected

def test_fuzzy_match_ranking(collection):
    text = 'mi'
    results = fuzzyfinder(text, collection)
    expected = ['migrations.py', 'django_migrations.py', 'django_admin_log.py']
    assert list(results) == expected

def test_fuzzy_match_greedy(collection):
    text = 'user'
    results = fuzzyfinder(text, collection)
    expected = ['user_group.doc', 'users.txt', 'api_user.doc']
    assert list(results) == expected

def test_fuzzy_integer_input(collection):
    text = 123
    results = fuzzyfinder(text, collection)
    expected = ['123.py', 'test123test.py']

def test_accessor(dict_collection):
    text = 'user'
    results = fuzzyfinder(text, dict_collection, lambda x: x['name'])
    expected = [{'name': 'user_group.doc'}, {'name': 'users.txt'}, {'name': 'api_user.doc'}]
    assert list(results) == expected
