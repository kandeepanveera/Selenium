""""
setup method:
-execute multiple time before every test method within class
teardown method:
  execute multiple time after every test method within class
setUpclass(cls)
-execute once class started
tearDownClass(cls)
-execute once class completed
setUpModule:
execute before module start
tearDownmodule:
execuet after module finish

"""

import unittest

def setUpModule():
    print("stUpModule")
def tearDownModule():
    print("tear down module")

class Apptesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Application started")#excute once the class started
    @classmethod
    def tearDownClass(cls):
        print("Apllication closed")#execute after class completed.

    @classmethod
    def setUp(self):
        print("Setup method will execute multiple times before every test")
    @classmethod
    def tearDown(self):
        print("Teardown method will execute multiple times after every test")

    def test_search(self):
        print("Google Search")
    def test_netbanking(self):
        print("Netbanking tested")
    def test_python(self):
        print("python tutorial")
if __name__=="__main__":
    unittest.main()
