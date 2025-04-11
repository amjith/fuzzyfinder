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
    return [
        "migrations.py",
        "django_migrations.py",
        "django_admin_log.py",
        "api_user.doc",
        "user_group.doc",
        "users.txt",
        "accounts.txt",
        "123.py",
        "test123test.py",
    ]


@pytest.fixture
def cased_collection():
    return [
        "MIGRATIONS.py",
        "django_MiGRations.py",
        "django_admin_log.py",
        "migrations.doc",
        "user_group.doc",
        "users.txt",
    ]


@pytest.fixture
def dict_collection():
    return [
        {"name": "migrations.py"},
        {"name": "django_migrations.py"},
        {"name": "django_admin_log.py"},
        {"name": "api_user.doc"},
        {"name": "user_group.doc"},
        {"name": "users.txt"},
        {"name": "accounts.txt"},
    ]


@pytest.fixture
def highlighting_collection():
    return ["fuuz", "fuz", "fufuz", "afbcfdzeuffzhijkl", "python"]


def test_substring_match(collection):
    text = "txt"
    results = fuzzyfinder(text, collection)
    expected = ["users.txt", "accounts.txt"]
    assert list(results) == expected


def test_case_insensitive_substring_match(cased_collection):
    text = "miGr"
    results = fuzzyfinder(text, cased_collection)
    expected = ["MIGRATIONS.py", "migrations.doc", "django_MiGRations.py"]
    assert list(results) == expected


def test_case_sensitive_substring_match(cased_collection):
    text = "MiGR"
    results = fuzzyfinder(text, cased_collection, ignore_case=False)
    expected = ["django_MiGRations.py"]
    assert list(results) == expected


def test_use_shortest_match_if_matches_overlap():
    collection_list = ["fuuz", "fuz", "fufuz"]
    text = "fuz"
    results = fuzzyfinder(text, collection_list)
    expected = ["fuz", "fufuz", "fuuz"]
    assert list(results) == expected


def test_substring_match_with_dot(collection):
    text = ".txt"
    results = fuzzyfinder(text, collection)
    expected = ["users.txt", "accounts.txt"]
    assert list(results) == expected


def test_fuzzy_match(collection):
    text = "djmi"
    results = fuzzyfinder(text, collection)
    expected = ["django_migrations.py", "django_admin_log.py"]
    assert list(results) == expected


def test_fuzzy_match_ranking(collection):
    text = "mi"
    results = fuzzyfinder(text, collection)
    expected = ["migrations.py", "django_migrations.py", "django_admin_log.py"]
    assert list(results) == expected


def test_fuzzy_match_greedy(collection):
    text = "user"
    results = fuzzyfinder(text, collection)
    expected = ["user_group.doc", "users.txt", "api_user.doc"]
    assert list(results) == expected


def test_fuzzy_integer_input(collection):
    text = 123
    results = fuzzyfinder(text, collection)
    expected = ["123.py", "test123test.py"]
    assert list(results) == expected


def test_accessor(dict_collection):
    text = "user"
    results = fuzzyfinder(text, dict_collection, lambda x: x["name"])
    expected = [{"name": "user_group.doc"}, {"name": "users.txt"}, {"name": "api_user.doc"}]
    assert list(results) == expected


def test_no_alpha_num_sort():
    collection = ["zzfuz", "nnfuz", "aafuz", "ttfuz", "wow!", "python"]
    text = "fuz"
    results = fuzzyfinder(text, collection, sort_results=False)
    expected = ["zzfuz", "nnfuz", "aafuz", "ttfuz"]
    assert list(results) == expected


def test_highlight_boolean_input(highlighting_collection):
    text = "fuz"
    results = fuzzyfinder(text, highlighting_collection, highlight=True)
    expected = [
        "\033[42mfuz\033[0m",
        "\033[42mfu\033[0mfu\033[42mz\033[0m",
        "\033[42mfu\033[0mu\033[42mz\033[0m",
        "a\033[42mf\033[0mbcfdze\033[42mu\033[0mff\033[42mz\033[0mhijkl",
    ]
    assert list(results) == expected


@pytest.mark.parametrize(
    ("color", "ansi_code"),
    [
        ("red", "\033[41m"),
        ("green", "\033[42m"),
        ("yellow", "\033[43m"),
        ("blue", "\033[44m"),
        ("magenta", "\033[45m"),
        ("cyan", "\033[46m"),
    ],
)
def test_highlight_string_input(highlighting_collection, color, ansi_code):
    text = "fuz"
    results = fuzzyfinder(text, highlighting_collection, highlight=color)
    expected = [
        f"{ansi_code}fuz\033[0m",
        f"{ansi_code}fu\033[0mfu{ansi_code}z\033[0m",
        f"{ansi_code}fu\033[0mu{ansi_code}z\033[0m",
        f"a{ansi_code}f\033[0mbcfdze{ansi_code}u\033[0mff{ansi_code}z\033[0mhijkl",
    ]
    assert list(results) == expected


def test_highlight_ansi_tuple_input(highlighting_collection):
    text = "fuz"
    bold_with_peach_bg = "\033[48;5;209m\033[1m", "\033[0m"
    results = fuzzyfinder(text, highlighting_collection, highlight=bold_with_peach_bg)
    expected = [
        "\033[48;5;209m\033[1mfuz\033[0m",
        "\033[48;5;209m\033[1mfu\033[0mfu\033[48;5;209m\033[1mz\033[0m",
        "\033[48;5;209m\033[1mfu\033[0mu\033[48;5;209m\033[1mz\033[0m",
        "a\033[48;5;209m\033[1mf\033[0mbcfdze\033[48;5;209m\033[1mu\033[0mff\033[48;5;209m\033[1mz\033[0mhijkl",
    ]
    assert list(results) == expected


def test_highlight_html_tuple_input(highlighting_collection):
    text = "fuz"
    html_class = "<span class='highlight'>", "</span>"
    results = fuzzyfinder(text, highlighting_collection, highlight=html_class)
    expected = [
        "<span class='highlight'>fuz</span>",
        "<span class='highlight'>fu</span>fu<span class='highlight'>z</span>",
        "<span class='highlight'>fu</span>u<span class='highlight'>z</span>",
        "a<span class='highlight'>f</span>bcfdze<span class='highlight'>u</span>ff<span class='highlight'>z</span>hijkl",
    ]
    assert list(results) == expected


def test_highlight_case_sensitive(cased_collection):
    text = "mi"
    parentheses = "(", ")"
    results = fuzzyfinder(text, cased_collection, ignore_case=False, highlight=parentheses)
    expected = [
        "(mi)grations.doc",
        "django_ad(mi)n_log.py",
    ]
    assert list(results) == expected
