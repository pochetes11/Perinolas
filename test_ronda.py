from ronda import Ronda
from jugador import Jugador
import pytest

def test_agregarJugador_funciona_correctamente():
    ronda = Ronda()
    jugador = Jugador("Mateo", 5)
    ronda.agregarJugador(jugador)
    assert jugador in ronda.jugadores

def test_agregarJugador_tira_error_sin_fichas():
    ronda = Ronda()
    jugador = Jugador("Janna", 0)
    with pytest.raises(ValueError):
        ronda.agregarJugador(jugador)

def test_sacarJugadoresSinFichas_elimina_correctamente():
    ronda = Ronda()
    jugador1 = Jugador("Martina", 0)
    jugador2 = Jugador("Lautaro", 0)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    ronda.sacarJugadoresSinFichas()
    assert jugador1  not in ronda.jugadores
    assert jugador2 not in ronda.jugadores

def test_jugadorEnTurno_devuelve_correctamente():
    ronda = Ronda()
    jugador1 = Jugador("Roma", 4)
    jugador2 = Jugador("Luna", 6)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    assert ronda.jugadorEnTurno() == jugador1

def test_pasarTurno_funciona_correctamente():
    ronda = Ronda()
    jugador1 = Jugador("Agustin", 3)
    jugador2 = Jugador("Sol", 5)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    ronda.pasarTurno()
    assert ronda.jugadorEnTurno() == jugador2

def test_quedaUnSoloJugador_devuelve_correctamente():
    ronda = Ronda()
    jugador = Jugador("Ariana", 2)
    ronda.agregarJugador(jugador)
    assert ronda.quedaUnSoloJugador()
    ronda.agregarJugador(Jugador("Matias", 4))
    assert not ronda.quedaUnSoloJugador()

def test_str_muestra_correctamente():
    ronda = Ronda()
    jugador1 = Jugador("Messi", 3)
    jugador2 = Jugador("Alvarez", 7)
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    assert str(ronda) == f"{jugador1}\n{jugador2}"
