import unittest
import graph


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.graf=graph.graph()
        self.graf.insert(1, 2, 3, 4)

    def test_reach_at_index(self):
        self.assertRaises(IndexError,self.graf.reach_at_index,2)
        # lazem y3y type error ??
        # self.assertRaisesRegex(IndexError,"index out of range >:(",self.graf.reach_at_index,2)


    def test_insert(self):
        self.assertEqual(len(self.graf),1)
        self.assertEqual(self.graf.reach_at_index(0),[1, 2, 3, 4])
        self.assertEqual(len(self.graf.reach_at_index(0)),4)

    def test_insert_at_index(self):
        self.graf.insert_at_index(0,6)

        self.assertEqual(self.graf.reach_at_index(0),[1,2,3,4,6])
        self.assertEqual(len(self.graf.reach_at_index(0)),5)

    def test_traverse(self):
        self.graf.insert(1, 2, 3, 4)




if __name__ == '__main__':
    unittest.main()
