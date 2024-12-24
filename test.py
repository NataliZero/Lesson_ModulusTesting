import unittest
from main import modulus

class TestModulus(unittest.TestCase):
    def test_modulus_success(self):
        # Проверка корректного остатка от деления
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(20, 5), 0)
        self.assertEqual(modulus(7, 2), 1)

    def test_modulus_by_zero(self):
        # Проверка обработки ошибки деления на ноль
        self.assertRaises(ValueError, modulus, 10, 0)

if __name__ == '__main__':
    unittest.main()
