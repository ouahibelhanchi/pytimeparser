#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pytimeparser.api` module"""

import datetime

import pytest

from pytimeparser import parse


def test_parse_empty():
    with pytest.raises(ValueError):
        parse('')


def test_parse_non_string():
    with pytest.raises(TypeError):
        parse(None)


def test_parse():
    output = parse('4 years, 3 months and 4 days')
    expected_output = datetime.timedelta(
        weeks=4*52+3*4, days=4,
    )
    assert output == expected_output


def test_parse_negative():
    output = parse('- 3 hours and 30 minutes and 300 microseconds')
    expected_output = datetime.timedelta(
        hours=-3, minutes=30, milliseconds=300*0.001
    )
    assert output == expected_output


def test_parse_whitespace():
    output = parse('-4    years  ,    \t 3 days   ')
    expected_output = datetime.timedelta(weeks=-4*52, days=3)
    assert output == expected_output


def test_parse_from_to():
    output = parse('3 to 4 days, 5 to 6 hours')
    expected_min = datetime.timedelta(days=3, hours=5)
    expected_max = datetime.timedelta(days=4, hours=6)
    assert expected_min <= output <= expected_max


def test_parse_free_text():
    output = parse('She said she will comback in 2 hours and 30 minutes')
    expected_output = datetime.timedelta(hours=2, minutes=30)
    assert output == expected_output


def test_parse_packed():
    output = parse('1w3d2h32m')
    expected_output = datetime.timedelta(weeks=1, days=3, hours=2, minutes=32)
    assert output == expected_output


def test_parse_packed_spaced():
    output = parse('1 w 3 d 2 h 32 m')
    expected_output = datetime.timedelta(weeks=1, days=3, hours=2, minutes=32)
    assert output == expected_output


def test_parse_duration():
    output = parse('2:04:13:2.266')
    expected_output = datetime.timedelta(
        hours=2, minutes=4, seconds=13, milliseconds=2, microseconds=266
    )
    assert output == expected_output


def test_parse_uptime_format():
    output = parse('2 days, 4:13:02')
    expected_output = datetime.timedelta(
        days=2, hours=4, minutes=13, seconds=2
    )
    assert output == expected_output


def test_parse_postgres_day_time_format():
    output = parse('3 days 04:05:06')
    expected_output = datetime.timedelta(
        days=3, hours=4, minutes=5, seconds=6
    )
    assert output == expected_output


def test_parse_iso_8601_duration_format():
    output = parse('P1Y2M3W10DT2H30M')
    expected_output = datetime.timedelta(
        weeks=1*52+2*4+3, days=10, hours=2, minutes=30
    )
    assert output == expected_output
