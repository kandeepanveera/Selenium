"""

This will be usefull when u r testing for list,tuple,set and dict
"""

import unittest

class Test(unittest.TestCase):
    def testName(self):
        list={"kandeepan","deepshika","baby"}
        self.assertIn("kandeepan",list)
        #self.assertNotIn("veera",list)


if __name__=="__main__":
    unittest.main()