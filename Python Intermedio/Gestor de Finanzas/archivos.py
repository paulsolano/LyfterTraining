import json
import os

_RUTA_MOVIMIENTOS = os.path.join(os.path.dirname(__file__), "movimientos.json")
_RUTA_CATEGORIAS = os.path.join(os.path.dirname(__file__), "categorias.json")

def _cargar(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

def _guardar(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

def cargar_movimientos():
    return _cargar(_RUTA_MOVIMIENTOS)

def guardar_movimientos(movimientos):
    _guardar(_RUTA_MOVIMIENTOS, movimientos)

def cargar_categorias():
    return _cargar(_RUTA_CATEGORIAS)

def guardar_categorias(categorias):
    _guardar(_RUTA_CATEGORIAS, categorias)
