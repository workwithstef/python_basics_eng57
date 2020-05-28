import unittest

def check_if_digit_div_num(digit, num_div):
    return digit % num_div == 0

# LHS: calling function with specific parameters. RHS: expected result
# print(check_if_digit_div_num(4, 2)) == True
# print(check_if_digit_div_num(5, 3)) == False
# print(check_if_digit_div_num(6, 4)) == False
# print(check_if_digit_div_num(8, 4)) == True



class Tests(unittest.TestCase):
    def test_div_num(self):
        self.assertEqual(check_if_digit_div_num(4, 2), True)
        self.assertTrue(check_if_digit_div_num(8, 2))
        self.assertFalse(check_if_digit_div_num(9, 5))
    def test_div_digit(self):
        self.assertEqual(check_if_digit_div_num(998, 1000), False)
        self.assertEqual(check_if_digit_div_num(5, 1), True)
        self.assertFalse(check_if_digit_div_num(7, 2))

if __name__ == '__main__':
    unittest.main()

