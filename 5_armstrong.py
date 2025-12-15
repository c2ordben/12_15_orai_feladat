import unittest

def armstrong(num:int)->bool:
    digits = str(num)
    n = len(digits)
    total = sum(int(digit) ** n for digit in digits)
    return total == num





class TestFibo(unittest.TestCase):
        def test_armstrong_true(self):
            self.assertTrue(armstrong(153))
            self.assertTrue(armstrong(9474))
            self.assertTrue(armstrong(370))

        def test_armstrong_false(self):
            self.assertFalse(armstrong(100))
            self.assertFalse(armstrong(200))
            self.assertFalse(armstrong(123))

        def test_single_digit(self):
            for i in range(10):
                self.assertTrue(armstrong(i))


if __name__ == "__main__":
    unittest.main()