"""

skip test
skip test with reason
skip test with condition

"""
import unittest

class Apptesting(unittest.TestCase):
    @unittest.SkipTest  # test case will be skipped
    def test_search(self):
        print("Google Search")
    @unittest.skip("With reason") #skipping with raeson
    def test_netbanking(self):
        print("Netbanking tested")
    @unittest.skipIf(1==1,"Numbers not equal") #skipping with condition
    def test_python(self):
        print("python tutorial")

    def test_java(self):
        print("Java tutorial")


if __name__ == "__main__":
    unittest.main()