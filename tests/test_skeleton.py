# -*- coding: utf-8 -*-

import pytest

from s3_log_query.skeleton import fib

__author__ = "mikethoun"
__copyright__ = "mikethoun"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
