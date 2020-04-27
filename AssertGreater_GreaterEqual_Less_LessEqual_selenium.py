import unittest

class Test(unittest.TestCase):
    def testName(self):
        self.assertGreater(100,10)
        self.assertGreaterEqual(100,100)
        self.assertLess(10,100)
        self.assertLessEqual(10,10)


if __name__=="__main__":
    unittest.main()