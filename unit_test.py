# coding=utf8
# Author: quheng

import pytest
import database

def test_database():
    assert database.test() == None
