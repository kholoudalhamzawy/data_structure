import unittest
import hash

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.hash_table=hash.hash_table()
        self.hash_table["march 28"]=23

    def test_insertion(self):
        self.assertEqual(hash.hash_table().hashing("march 26"), hash.hash_table().hashing("march 17"))
        self.hash_table["march 26"] = 60
        self.hash_table["march 17"] = 70
        self.assertEqual(self.hash_table["march 26"], 60)


    def test_hashing(self):
        self.assertEqual(hash.hash_table().hashing("march 28"), 61)
        self.assertRaisesRegex(TypeError,"key must be string",hash.hash_table().hashing,33)

    def test_del(self):
        del self.hash_table["march 28"]
        self.assertEqual(self.hash_table["march 28"],None)



if __name__ == '__main__':
    unittest.main()
