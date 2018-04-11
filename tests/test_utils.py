#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pytimeparser.utils` module."""


from pytimeparser import utils


def test_remove_whitespace():
    output = utils.remove_whitespace('  this \t\r  is\fa\ntext  ')
    expected_output = 'thisisatext'
    assert output == expected_output


def test_normalize_whitespace():
    output = utils.normalize_whitespace('this    is  \n\f\t\r   a test')
    expected_output = 'this is a test'
    assert output == expected_output


def test_normalize_numbers():
    output = utils.normalize_numbers('text -\t112\f323 . 456 another +32 . 03')
    expected_output = 'text -112323.456 another +32.03'
    assert output == expected_output


def test_mapping_inversed():
    output = utils.mapping_inversed(dict(a=['aa', 'aaa'], b=['bb']))
    expected_output = {'aaa': 'a', 'aa': 'a', 'bb': 'b'}
    assert output == expected_output


def test_mapping_to_list():
    output = utils.mapping_to_list(dict(a='aa', b='bb', c='cc'))
    expected_output = ['a', 'b', 'c', 'aa', 'bb', 'cc']
    assert output.sort() == expected_output.sort()
