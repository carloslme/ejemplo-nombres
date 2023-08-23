import sys
from pathlib import Path

import pytest

from ejemplo.app.funciones import (generar_usuario, procesar_apellido_materno,
                                   procesar_apellido_paterno, procesar_nombre)

# Add root to sys.path
# https://fortierq.github.io/python-import/
path_root = Path(__file__).parents[3]
sys.path.append(str(path_root))


def concatenar_nombre_completo(nombre, ap, am):
    return nombre + " " + ap + " " + am


def obtener_datos_test_integracion():
    return [
        ("carlos", "LOPEZ", "meJIa", "Carlos Lopez Mejia", "car.lopm"),
        ("ivan", "huERTA", "CoroNA", "Ivan Huerta Corona", "iva.huec"),
    ]


@pytest.mark.parametrize(
    "nombre, ap, am, esperado, usuario", obtener_datos_test_integracion()
)
def test_divide_parametrize(nombre, ap, am, esperado, usuario):
    nombre_procesado = procesar_nombre(nombre)
    ap_procesado = procesar_apellido_paterno(ap)
    am_procesado = procesar_apellido_materno(am)

    assert (
        nombre_procesado
        + " "
        + ap_procesado
        + " "
        + am_procesado
        + " "
        + generar_usuario(nombre_procesado, ap_procesado, am_procesado)
        == f"{esperado} {usuario}"
    )
