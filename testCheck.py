import unittest
import findx
class TestFind_x(unittest.TestCase):
    def testCase(self):
        temp = (5,5)
        self.assertEqual(findx.find_x(*temp),"Done")
        temp = (0,5)
        self.assertEqual(findx.find_x(*temp),"None")
        temp = (0,5)
        self.assertEqual(findx.find_x(*temp),"All")

if __name__ == '__main__':
    unittest.main()