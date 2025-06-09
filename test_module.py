import unittest
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):

    def test_valid_input(self):
        input_list = [0,1,2,3,4,5,6,7,8]
        result = calculate(input_list)
        self.assertEqual(result['mean'][2], 4.0)
        self.assertEqual(result['max'][2], 8)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == '__main__':
    unittest.main()
