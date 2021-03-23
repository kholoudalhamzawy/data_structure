import unittest
import sort

class test_buble(unittest.TestCase):
    def test_buble(self):
        self.assertEqual(sort.buble([3,4,2,6,6,1]),[1,2,3,4,6,6])
        self.assertEqual(len(sort.buble([3,4,2,6,1,6])),6)


class test_selection(unittest.TestCase):
    def test_selection(self):
        self.assertEqual(sort.selection([3,4,2,6,6,1]),[1,2,3,4,6,6])
        self.assertEqual(len(sort.selection([3,4,2,6,1,6])),6)



class test_insertion(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(sort.insertion([3,4,2,6,6,1]),[1,2,3,4,6,6])
        self.assertEqual(len(sort.insertion([3,4,2,6,1,6])),6)


class test_merge(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(sort.merge([3,4,2,6,6,1]),[1,2,3,4,6,6])
        self.assertEqual(len(sort.merge([3,4,2,6,6,1])),6)


class test_quick(unittest.TestCase):
    def test_partion(self):
        self.assertEqual(sort.partition([3, 7, 2, 1, 5, 4], 0, 5), 3)
    def test_quick(self):
        self.assertEqual(sort.quick([3,7,2,1,5,4],0,5),[1,2,3,4,5,7])
        self.assertEqual(len(sort.quick([3,4,2,6,6,1],0,5)),6)

class test_binary(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(sort.binary([3,7,2,1,5,4]),[1,2,3,4,5,7])
        self.assertEqual(len(sort.binary([3,4,2,6,6,1])),6)

class test_heap(unittest.TestCase):
    def test_max_heap(self):
        self.assertEqual(sort.max_heap([12,8,17,7,15,19,6,22]),[22,19,17,15,8,12,6,7])
    def test_heap(self):
        self.assertEqual(sort.heap([3,7,2,1,5,4]),[1,2,3,4,5,7])
    def test_heap_sort(self):
        self.assertEqual(sort.heap_sort([3,7,2,1,5,4]),[1,2,3,4,5,7])

if __name__ == '__main__':
    unittest.main()
