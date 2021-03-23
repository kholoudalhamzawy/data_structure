
import unittest
import search

class test_jump(unittest.TestCase):
    def test_jump(self):
        self.assertEqual(search.jump([3, 4, 2, 6, 6, 1],6,6), 5)
        self.assertEqual(search.jump([3, 4, 2, 6, 6, 1],6,4), 4)
        self.assertEqual(search.jump([3, 4, 2, 6, 6, 1],6,9), -1)




if __name__=='__main__':
    unittest.main()