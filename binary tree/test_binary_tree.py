import unittest, binary_tree

class test_binary_tree(unittest.TestCase):

    def setUp(self):
        self.tree = binary_tree.binary_tree()
        self.tree(12, 8, 7, 3, 7, 17, 15, 14, 16, 19, 18, 20)
        self.empty_tree=binary_tree.binary_tree()


    def test_binary_tree(self):
        self.assertEqual(self.tree.count,12)
        self.assertEqual(len(self.tree),12)



    def test_add(self):
        self.tree.add(3)
        self.assertEqual(self.tree.count,13)
        self.assertEqual(len(self.tree),13)



    def test_ordered_tree(self):
        self.assertEqual(self.tree.ordered_tree(),[12, 8, 7, 3, 7, 17, 15, 14, 16, 19, 18, 20])
        #to test raising errors it should be put in a container, so the return value could be combared
        #in this case the container is 'lambda' or 'with'
        self.assertRaises(Exception,lambda:self.empty_tree.ordered_tree())
        with self.assertRaises(Exception):self.empty_tree.ordered_tree()


    def test_sorted_tree(self):
        self.assertEqual(self.tree.sorted_tree(),[3, 7, 7, 8, 12, 14, 15, 16, 17, 18, 19, 20])
        with self.assertRaises(Exception):self.empty_tree.sorted_tree()

    def test_delete_whole_tree(self):
        self.tree.delete_whole_tree()
        self.assertEqual(self.tree.count,0)
        self.assertEqual(len(self.tree),0)
        with self.assertRaises(Exception): self.empty_tree.delete_whole_tree()

    def test_delete_node(self):
        self.tree.delete_node(8)
        self.assertEqual(self.tree.count,11)
        self.assertEqual(len(self.tree),11)
        self.assertEqual(self.tree.list,[12, 7, 3, 7, 17, 15, 14, 16, 19, 18, 20])
        with self.assertRaises(Exception):self.tree.delete_node(90)
        with self.assertRaises(Exception):self.empty_tree.delete_node(3)




if __name__=='__main__':
    unittest.main()