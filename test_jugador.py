from jugador import Jugador
import pytest

def test_dar_ficha_agrega_correctamente():
    jugador = Jugador("Sol", 8)
    jugador.darFicha(3)
    assert jugador.fichas == 11

def test_sacar_ficha_quita_correctamente():
    jugador = Jugador("Luna", 6)
    jugador.sacarFicha(2)
    assert jugador.fichas == 4

def test_tiene_ficha_funciona_correctamente():
    jugador = Jugador("Roma", 10)
    assert jugador.tieneFicha(5)
    assert not jugador.tieneFicha(12)

def test_sin_fichas_devuelve_correctamente():
    jugador = Jugador("Ares", 3)
    assert not jugador.sinFichas()
    jugador.sacarFicha(3)
    assert jugador.sinFichas()

def test_str_muestra_correctamente():
    jugador = Jugador("Apolo", 7)
