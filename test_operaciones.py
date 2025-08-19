import unittest
from operaciones import sumar

class TestOperaciones(unittest.TestCase):
    def test_suma_numeros_enteros(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

    def test_suma_numeros_decimales(self):
        self.assertAlmostEqual(sumar(2.5, 3.7), 6.2)
        self.assertAlmostEqual(sumar(0.1, 0.2), 0.3)

    def test_suma_tipos_invalidos(self):
        with self.assertRaises(TypeError):
            sumar("2", 3)
        with self.assertRaises(TypeError):
            sumar(2, "3")
        with self.assertRaises(TypeError):
            sumar("a", "b")

if __name__ == '__main__':
    unittest.main()