from apuesta import Apuesta
import pytest

def test_ponerFicha_agrega_correctamente():
    apuesta = Apuesta()
    apuesta.ponerFicha(3)
    assert apuesta.fichas == 3

def test_tomarFicha_quita_correctamente():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    apuesta.tomarFicha(3)
    assert apuesta.fichas == 2

def test_tomarTodas_devuelve_correctamente():
    apuesta = Apuesta()
    apuesta.ponerFicha(7)
    todas = apuesta.tomarTodas()
    assert todas == 7
    assert apuesta.fichas == 0

def test_tieneFicha_funciona_correctamente():
    apuesta = Apuesta()
    apuesta.ponerFicha(4)
    assert apuesta.tieneFicha(2)
    assert not apuesta.tieneFicha(6)

def test_estaVacia_devuelve_correctamente():
    apuesta = Apuesta()
    assert apuesta.estaVacia()
    apuesta.ponerFicha(2)
    assert not apuesta.estaVacia()

def test_str_muestra_correctamente():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    assert str(apuesta) == "Apuesta: 5 fichas"
