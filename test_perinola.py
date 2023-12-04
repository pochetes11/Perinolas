from perinola import Perinola
import pytest

def test_tirar_cambia_cara_visible():
    perinola = Perinola()
    cara_inicial = perinola.cara_visible
    perinola.tirar()
    nueva_cara = perinola.cara_visible
    assert cara_inicial != nueva_cara

def test_str_muestra_correctamente():
    perinola = Perinola()
    assert str(perinola) == f"Salio: {perinola.cara_visible}"
