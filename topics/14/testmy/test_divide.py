# python -m unittest -v test_divide.py
# python -m coverage run -m unittest test_divide.py
# coverage report

import unittest
import dividemod
from parameterized import parameterized


class Test1(unittest.TestCase):
    
    @parameterized.expand([
        [15, 3, 5.0],
        [2, 5, 0.4],
        [6, 3, 2.0]
    ])
    def test_parameterized(self, first, second, result):
        self.assertEqual(dividemod.divide(first,second), result)
    
    def test_possitive_divide(self):
        expected = 5.0
        actual = dividemod.divide(15,3)
        self.assertEqual(actual, expected)    

    def test_fract_divide(self):
        expected = 0.4
        actual = dividemod.divide(2,5)
        self.assertEqual(actual, expected)   
    
    def test_double_divide(self):
        expected = 0.3333
        actual = dividemod.divide(1,3)
        self.assertAlmostEqual(actual, expected, 4)
   
    def test_raises(self):
        self.assertRaises(Exception, dividemod, 3, 0)   

    
#test_another_function
    def another_function(self):
        self.assertTrue(False)

#########################################

# @parameterized.expand([
#         [15, 3, 5.0],
#         [2, 5, 0.4]
#     ])

#     def test_parameterized(self, first, second, result):
#         self.assertEqual(divide.divide(first,second), result)

if __name__ == '__main__':
    unittest.main()
