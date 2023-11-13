import unittest
from perinola import Perinola

class TestPerinola(unittest.TestCase):
    def test_tirar_cambia_cara_visible(self):
        perinola = Perinola()
        cara_inicial = perinola.cara_visible
        perinola.tirar()
        nueva_cara = perinola.cara_visible
        self.assertNotEqual(cara_inicial, nueva_cara)

    def test_str_muestra_correctamente(self):
        perinola = Perinola()
        self.assertEqual(str(perinola), f"Salio: {perinola.cara_visible}")

if __name__ == '__main__':
    unittest.main()
