import re
from datetime import datetime

import FreeSimpleGUI as sg
import files
import logic
import validations

_PARTIAL_AMOUNT_PATTERN = re.compile(r"^\d*\.?\d*$")
_MAX_TITLE = 50
_MAX_CATEGORY = 30

def _is_partial_amount_valid(text):
    return bool(_PARTIAL_AMOUNT_PATTERN.match(text))

def run():
    manager = _load_manager()
    displayed_movements = manager.get_all_movements()
    headings = ["Fecha", "Monto", "Título", "Categoría", "Tipo"]

    layout = [
        [sg.Button("Agregar Categoría"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso")],
        [
            sg.Text("Fecha inicio"),
            sg.pin(sg.Input(key="-START_DATE-", visible=False)),
            sg.CalendarButton("📅", target="-START_DATE-", format=validations.DATE_FORMAT, no_titlebar=False),
            sg.Text("Fecha fin"),
            sg.pin(sg.Input(key="-END_DATE-", visible=False)),
            sg.CalendarButton("📅", target="-END_DATE-", format=validations.DATE_FORMAT, no_titlebar=False),
            sg.Button("Filtrar"), sg.Button("Mostrar Todos"),
        ],
        [sg.Table(values=_table(displayed_movements), headings=headings, key="-TABLE-", auto_size_columns=True, justification="left", expand_x=True, expand_y=True, num_rows=10)],
        [sg.Text(_balance_text(manager), key="-BALANCE-")],
        [sg.Button("Borrar"), sg.Button("Salir")],
    ]
    window = sg.Window("Gestor de Finanzas", layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Salir"):
            break

        if event == "Agregar Categoría":
            _handle_add_category(manager)

        elif event in ("Agregar Gasto", "Agregar Ingreso"):
            movement_type = "Gasto" if event == "Agregar Gasto" else "Ingreso"
            result = _handle_add_movement(manager, window, movement_type)
            if result is not None:
                displayed_movements = result

        elif event == "Filtrar":
            result = _handle_filter(manager, window, values)
            if result is not None:
                displayed_movements = result

        elif event == "Mostrar Todos":
            displayed_movements = _handle_show_all(manager, window)

        elif event == "Borrar":
            displayed_movements = _handle_delete(manager, window, displayed_movements, values["-TABLE-"])

    window.close()

def _load_manager():
    manager = logic.FinanceManager()
    for name in files.load_categories():
        manager.add_category(name)

    saved_movements = files.load_movements()
    missing_categories = sorted({
        data["categoria"] for data in saved_movements if data["categoria"] not in manager.get_categories()
    })
    if missing_categories:
        for name in missing_categories:
            manager.add_category(name)
        files.save_categories(manager.get_categories())
        sg.popup("Aviso", f"Se reconstruyeron estas categorías a partir de movimientos ya guardados: {', '.join(missing_categories)}.")

    for data in saved_movements:
        date = data.get("fecha", datetime.now().strftime(validations.DATE_FORMAT))
        manager.add_movement(data["monto"], data["titulo"], data["categoria"], data["tipo"], date)

    return manager

def _save_movements(manager):
    files.save_movements([m.to_dict() for m in manager.get_all_movements()])

def _handle_add_category(manager):
    new_category = _add_category_window(manager.get_categories())
    if new_category:
        manager.add_category(new_category)
        files.save_categories(manager.get_categories())

def _handle_add_movement(manager, window, movement_type):
    categories = manager.get_categories()
    if not categories:
        sg.popup_error("Error", f"No hay categorías disponibles. Agrega una categoría antes de registrar un {movement_type.lower()}.")
        return None

    data = _add_movement_window(movement_type, categories)
    if not data:
        return None

    amount, title, category, date = data
    try:
        manager.add_movement(amount, title, category, movement_type, date)
    except ValueError as error:
        sg.popup_error("Error", str(error))
        return None

    _save_movements(manager)
    displayed_movements = manager.get_all_movements()
    window["-TABLE-"].update(values=_table(displayed_movements))
    window["-BALANCE-"].update(_balance_text(manager))
    return displayed_movements

def _handle_filter(manager, window, values):
    start_date = values["-START_DATE-"]
    end_date = values["-END_DATE-"]
    if not validations.is_valid_date(start_date) or not validations.is_valid_date(end_date):
        sg.popup_error("Error", "Las fechas deben tener el formato dd/mm/yyyy.")
        return None

    try:
        filtered_movements = manager.get_movements_in_range(start_date, end_date)
    except ValueError as error:
        sg.popup_error("Error", str(error))
        return None

    window["-TABLE-"].update(values=_table(filtered_movements))
    return filtered_movements

def _handle_show_all(manager, window):
    displayed_movements = manager.get_all_movements()
    window["-TABLE-"].update(values=_table(displayed_movements))
    return displayed_movements

def _handle_delete(manager, window, displayed_movements, selected):
    if not selected:
        sg.popup_error("Error", "Selecciona primero una fila de la tabla para borrarla.")
        return displayed_movements

    for index in selected:
        manager.remove_movement(displayed_movements[index])

    _save_movements(manager)
    displayed_movements = manager.get_all_movements()
    window["-TABLE-"].update(values=_table(displayed_movements))
    window["-BALANCE-"].update(_balance_text(manager))
    return displayed_movements

def _balance_text(manager):
    return f"Balance: ₡{manager.calculate_balance():.2f}"

def _table(movements):
    rows = []
    for data in (m.to_dict() for m in movements):
        rows.append([data["fecha"], f"₡{data['monto']:.2f}", data["titulo"], data["categoria"], data["tipo"]])
    return rows

def _add_category_window(existing_categories):
    layout = [
        [sg.Text("Nombre de la categoría"), sg.Input(key="-NAME-", enable_events=True)],
        [sg.pin(sg.Text(f"Máximo {_MAX_CATEGORY} caracteres", text_color="red", key="-NAME_WARNING-", visible=False))],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    window = sg.Window("Agregar Categoría", layout, modal=True)
    category = None
    existing_names = {name.lower() for name in existing_categories}

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "-NAME-":
            if len(values["-NAME-"]) > _MAX_CATEGORY:
                window["-NAME-"].update(values["-NAME-"][:_MAX_CATEGORY])
            window["-NAME_WARNING-"].update(visible=len(values["-NAME-"]) >= _MAX_CATEGORY)

        if event == "Guardar":
            name = values["-NAME-"].strip()
            if not name:
                sg.popup_error("Error", "Debes escribir un nombre de categoría.")
            elif name.lower() in existing_names:
                sg.popup_error("Error", f"La categoría '{name}' ya existe.")
            else:
                category = name
                break

    window.close()
    return category

def _add_movement_window(movement_type, categories):
    today = datetime.now().strftime(validations.DATE_FORMAT)
    layout = [
        [sg.Text("Título"), sg.Input(key="-TITLE-", enable_events=True)],
        [sg.Text("Monto"), sg.Text("₡"), sg.Input(key="-AMOUNT-", enable_events=True)],
        [sg.pin(sg.Text(f"Máximo {_MAX_TITLE} caracteres para el título", text_color="red", key="-TITLE_WARNING-", visible=False))],
        [sg.Text("Categoría"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
        [sg.Text("Fecha (dd/mm/yyyy)"), sg.Input(today, key="-DATE-"), sg.CalendarButton("📅", target="-DATE-", format=validations.DATE_FORMAT, no_titlebar=False)],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    window = sg.Window(f"Agregar {movement_type}", layout, modal=True)
    data = None
    last_valid_amount = ""

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "-TITLE-":
            if len(values["-TITLE-"]) > _MAX_TITLE:
                window["-TITLE-"].update(values["-TITLE-"][:_MAX_TITLE])
            window["-TITLE_WARNING-"].update(visible=len(values["-TITLE-"]) >= _MAX_TITLE)

        if event == "-AMOUNT-":
            if _is_partial_amount_valid(values["-AMOUNT-"]):
                last_valid_amount = values["-AMOUNT-"]
            else:
                window["-AMOUNT-"].update(last_valid_amount)

        if event == "Guardar":
            title = values["-TITLE-"].strip()
            if not title or not values["-AMOUNT-"] or not values["-CATEGORY-"] or not values["-DATE-"]:
                sg.popup_error("Error", "Completa título, monto, categoría y fecha antes de guardar.")
            elif values["-CATEGORY-"] not in categories:
                sg.popup_error("Error", f"La categoría '{values['-CATEGORY-']}' no existe. Selecciona una de la lista.")
            elif not validations.is_valid_date(values["-DATE-"]):
                sg.popup_error("Error", "La fecha debe tener el formato dd/mm/yyyy.")
            elif not validations.is_not_future_date(values["-DATE-"]):
                sg.popup_error("Error", "La fecha no puede ser una fecha futura.")
            elif not validations.is_valid_amount(values["-AMOUNT-"]):
                sg.popup_error("Error", "El monto debe ser un número mayor que cero.")
            else:
                data = (values["-AMOUNT-"], title, values["-CATEGORY-"], values["-DATE-"])
                break

    window.close()
    return data
