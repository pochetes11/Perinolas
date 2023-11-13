import unittest
from ronda import Ronda
from jugador import Jugador

class TestRonda(unittest.TestCase):
    def test_agregarJugador_funciona_correctamente(self):
        ronda = Ronda()
        jugador = Jugador("Mateo", 5)
        ronda.agregarJugador(jugador)
        self.assertIn(jugador, ronda.jugadores)

    def test_agregarJugador_tira_error_sin_fichas(self):
        ronda = Ronda()
        jugador = Jugador("Janna", 0)
        with self.assertRaises(ValueError):
            ronda.agregarJugador(jugador)

    def test_sacarJugadoresSinFichas_elimina_correctamente(self):
        ronda = Ronda()
        jugador1 = Jugador("Martina", 3)
        jugador2 = Jugador("Lautaro", 0)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        ronda.sacarJugadoresSinFichas()
        self.assertIn(jugador1, ronda.jugadores)
        self.assertNotIn(jugador2, ronda.jugadores)

    def test_jugadorEnTurno_devuelve_correctamente(self):
        ronda = Ronda()
        jugador1 = Jugador("Roma", 4)
        jugador2 = Jugador("Luna", 6)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        self.assertEqual(ronda.jugadorEnTurno(), jugador1)

    def test_pasarTurno_funciona_correctamente(self):
        ronda = Ronda()
        jugador1 = Jugador("Agustin", 3)
        jugador2 = Jugador("Sol", 5)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        ronda.pasarTurno()
        self.assertEqual(ronda.jugadorEnTurno(), jugador2)

    def test_quedaUnSoloJugador_devuelve_correctamente(self):
        ronda = Ronda()
        jugador = Jugador("Ariana", 2)
        ronda.agregarJugador(jugador)
        self.assertTrue(ronda.quedaUnSoloJugador())
        ronda.agregarJugador(Jugador("Matias", 4))
        self.assertFalse(ronda.quedaUnSoloJugador())

    def test_str_muestra_correctamente(self):
        ronda = Ronda()
        jugador1 = Jugador("Messi", 3)
        jugador2 = Jugador("Alvarez", 7)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        self.assertEqual(str(ronda), f"{jugador1}\n{jugador2}")

if __name__ == '__main__':
    unittest.main()
