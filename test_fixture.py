"""
pytest.fixture ==>Execute specific method before every test excute
pytest.yield.fixture ==>Execute specific method after every test excute

"""

import pytest

@pytest.fixture()
def setup():
    print("Once before every method")
def testmethod1(setup):
    print("This is test method1")
def testmethod2(setup):
    print("This is test menthod2")

