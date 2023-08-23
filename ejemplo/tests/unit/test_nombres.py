import sys
from pathlib import Path

import pytest

from ejemplo.app.funciones import (generar_usuario, procesar_apellido_materno,
                                   procesar_apellido_paterno, procesar_nombre)

# Add root to sys.path
# https://fortierq.github.io/python-import/
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))


# Pruebas para el nombre
def obtener_datos_test_nombre():
    return [("carlos", "Carlos"), ("MiGuel", "Miguel"), ("iVAN", "Ivan")]


@pytest.mark.parametrize("nombre, esperado", obtener_datos_test_nombre())
def test_nombre_parametrize(nombre, esperado):
    assert procesar_nombre(nombre) == esperado


# Pruebas para el apellido paterno
def obtener_datos_test_ap():
    return [("LOPEZ", "Lopez"), ("GarCIA", "Garcia"), ("sancHEz", "Sanchez")]


@pytest.mark.parametrize("ap, esperado", obtener_datos_test_ap())
def test_ap_parametrize(ap, esperado):
    assert procesar_apellido_paterno(ap) == esperado


# Pruebas para el apellido materno
def obtener_datos_test_am():
    return [("ferrer", "Ferrer"), ("SILVa", "Silva"), ("PalafoX", "Palafox")]


@pytest.mark.parametrize("am, esperado", obtener_datos_test_am())
def test_am_parametrize(am, esperado):
    assert procesar_apellido_materno(am) == esperado


# Pruebas para generar usuario
def obtener_datos_test_usuario():
    return [
        ("carlos", "LOPEZ", "meJIa", "car.lopm"),
        ("ivan", "huERTA", "CoroNA", "iva.huec"),
    ]


@pytest.mark.parametrize("nombre, ap, am, esperado",
                         obtener_datos_test_usuario())
def test_usuario_parametrize(nombre, ap, am, esperado):
    assert generar_usuario(nombre, ap, am) == esperado
