"""

pytest.yield.fixture ==>Execute specific method after every test excute

"""

import pytest
import HtmlTestRunner

@pytest.yield_fixture()
def setup():
    print("Once before every method")
    yield
    print("Once After every method")
def testmethod1(setup):
    print("This is test method1")

def testmethod2(setup):
    print("This is test menthod2")

