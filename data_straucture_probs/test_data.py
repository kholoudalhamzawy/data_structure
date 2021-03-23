import unittest
import data_structure_exe

class testdata(unittest.TestCase):

    def setUp(self):
        self.stack = data_structure_exe.new_stack()
        self.stack.size(4)
        self.stack.push(5)

    def test_push(self):
        self.stack.push(5)
        self.assertEqual(len(self.stack),2)

    def test_pop(self):
        self.stack.pop()
        self.assertEqual(len(self.stack),0)


    def test_postfix(self):
        self.assertEqual(data_structure_exe.postfix_evaluation((1,2,"+",3,5,"*",4,3)),3)


    def test_static_stack_split(self):
        self.stack=data_structure_exe.new_stack()
        self.stack.size(6)
        self.stack.push(1)
        self.stack.push(3)
        self.stack.push(5)
        self.first_stack = data_structure_exe.new_stack()
        self.first_stack.size(3)
        self.first_stack.push(1)
        self.first_stack.push(3)
        self.second_stack = data_structure_exe.new_stack()
        self.second_stack.size(3)
        self.second_stack.push(5)
        self.assertEqual(data_structure_exe.static_stack_split(self.stack,3),(self.first_stack.arr,self.second_stack.arr))


    def test_palindrome(self):
        self.assertEqual(data_structure_exe.palindrome("maAsa am"),True)
        self.assertEqual(data_structure_exe.palindrome("masaam"),False)


    def test_dublicate(self):
        self.dub = data_structure_exe.new_stack()
        self.dub.size(4)
        self.dub.push('a')
        self.dub.push('b')
        self.dub.push('b')
        self.char = data_structure_exe.new_stack()
        self.char.size(4)
        self.char.push('a')
        self.char.push('b')
        self.int = data_structure_exe.new_stack()
        self.int.size(4)
        self.int.push(1)
        self.int.push(2)
        self.assertListEqual(data_structure_exe.dublicate(self.char,self.int),self.dub.arr)


    def test_average(self):
        self.assertEqual(data_structure_exe.average([6, 2, 4, 8]),5.0)


    def test_mirror(self):
        self.q = data_structure_exe.new_queue()
        self.q.size(4)
        self.q.enqueue(6)
        self.q.enqueue(2)
        self.mirrorr=data_structure_exe.new_queue()
        self.mirrorr.size(6)
        self.mirrorr.enqueue(6)
        self.mirrorr.enqueue(2)
        self.mirrorr.enqueue(2)
        self.mirrorr.enqueue(6)
        self.assertEqual(data_structure_exe.mirror(self.q),self.mirrorr.arr)


    def test_anagrams(self):
        self.assertEqual(data_structure_exe.anagrams("post","stop"),True)
        self.assertEqual(data_structure_exe.anagrams("posst","stpop"),False)


    def test_is_palindrome(self):
        self.assertEqual(data_structure_exe.is_palindrome("mam"),True)
        self.assertEqual(data_structure_exe.is_palindrome("msam"),False)


    def test_shift_the_zero(self):
        self.stack = data_structure_exe.new_stack()
        self.stack.push(0)
        self.stack.push(5)
        self.stack.push(6)
        self.dub = data_structure_exe.new_stack()
        self.dub.push(5)
        self.dub.push(6)
        self.dub.push(0)
        self.assertEqual(data_structure_exe.shift_the_zero(self.stack),self.dub.arr)



if __name__=='__main__':
    unittest.main()
