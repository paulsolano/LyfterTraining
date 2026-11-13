import json
import os

_MOVEMENTS_PATH = os.path.join(os.path.dirname(__file__), "movimientos.json")
_CATEGORIES_PATH = os.path.join(os.path.dirname(__file__), "categorias.json")

def _load(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def _save(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def load_movements():
    return _load(_MOVEMENTS_PATH)

def save_movements(movements):
    _save(_MOVEMENTS_PATH, movements)

def load_categories():
    return _load(_CATEGORIES_PATH)

def save_categories(categories):
    _save(_CATEGORIES_PATH, categories)
