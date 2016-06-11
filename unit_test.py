# coding=utf8
# Author: quheng

import pytest
import database

def test_database():
    """
    test database connection
    """
    assert database.test()
