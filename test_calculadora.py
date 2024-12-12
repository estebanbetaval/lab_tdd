import unittest
from calculadora import suma, resta, multiplica, divide

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 1), -1)

    def test_multiplica(self):
        self.assertEqual(multiplica(2, 3), 6)
        self.assertEqual(multiplica(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()