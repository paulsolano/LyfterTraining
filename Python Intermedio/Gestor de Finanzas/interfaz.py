import re
from datetime import datetime

import FreeSimpleGUI as sg
import archivos
import logica

_PATRON_MONTO_PARCIAL = re.compile(r"^\d*\.?\d*$")
_MAX_TITULO = 50
_MAX_CATEGORIA = 30
_FORMATO_FECHA = "%d/%m/%Y"

def _es_monto_parcial_valido(texto):
    return bool(_PATRON_MONTO_PARCIAL.match(texto))

def _es_fecha_valida(texto):
    try:
        datetime.strptime(texto, _FORMATO_FECHA)
        return True
    except ValueError:
        return False

def ejecutar():
    gestor = logica.GestorFinanzas()
    for nombre in archivos.cargar_categorias():
        gestor.agregar_categoria(nombre)
    for fila in archivos.cargar_movimientos():
        monto, titulo, categoria, tipo = fila[:4]
        fecha = fila[4] if len(fila) > 4 else datetime.now().strftime(_FORMATO_FECHA)
        gestor.agregar_movimiento(monto, titulo, categoria, tipo, fecha)

    movimientos_mostrados = gestor.obtener_todos_los_movimientos()
    headings = ["Fecha", "Monto", "Título", "Categoría", "Tipo"]

    layout = [
        [sg.Button("Agregar Categoría"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso")],
        [
            sg.Text("Fecha inicio"),
            sg.pin(sg.Input(key="-FECHA_INICIO-", visible=False)),
            sg.CalendarButton("📅", target="-FECHA_INICIO-", format=_FORMATO_FECHA, no_titlebar=False),
            sg.Text("Fecha fin"),
            sg.pin(sg.Input(key="-FECHA_FIN-", visible=False)),
            sg.CalendarButton("📅", target="-FECHA_FIN-", format=_FORMATO_FECHA, no_titlebar=False),
            sg.Button("Filtrar"), sg.Button("Mostrar Todos"),
        ],
        [sg.Table(values=_tabla(movimientos_mostrados), headings=headings, key="-TABLA-", auto_size_columns=True, justification="left", expand_x=True, expand_y=True, num_rows=10)],
        [sg.Button("Borrar"), sg.Button("Salir")],
    ]
    window = sg.Window("Gestor de Finanzas", layout, resizable=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Salir"):
            break

        if event == "Agregar Categoría":
            nueva_categoria = _ventana_agregar_categoria()
            if nueva_categoria:
                gestor.agregar_categoria(nueva_categoria)
                archivos.guardar_categorias(gestor.obtener_categorias())

        if event in ("Agregar Gasto", "Agregar Ingreso"):
            tipo = "Gasto" if event == "Agregar Gasto" else "Ingreso"
            categorias = gestor.obtener_categorias()
            if not categorias:
                sg.popup_error("Error", f"No hay categorías disponibles. Agrega una categoría antes de registrar un {tipo.lower()}.")
            else:
                datos = _ventana_agregar_movimiento(tipo, categorias)
                if datos:
                    monto, titulo, categoria, fecha = datos
                    gestor.agregar_movimiento(monto, titulo, categoria, tipo, fecha)
                    archivos.guardar_movimientos([m.a_lista() for m in gestor.obtener_todos_los_movimientos()])
                    movimientos_mostrados = gestor.obtener_todos_los_movimientos()
                    window["-TABLA-"].update(values=_tabla(movimientos_mostrados))

        if event == "Filtrar":
            fecha_inicio = values["-FECHA_INICIO-"]
            fecha_fin = values["-FECHA_FIN-"]
            if not _es_fecha_valida(fecha_inicio) or not _es_fecha_valida(fecha_fin):
                sg.popup_error("Error", "Las fechas deben tener el formato dd/mm/yyyy.")
            else:
                movimientos_mostrados = gestor.obtener_movimientos_en_rango(fecha_inicio, fecha_fin)
                window["-TABLA-"].update(values=_tabla(movimientos_mostrados))

        if event == "Mostrar Todos":
            movimientos_mostrados = gestor.obtener_todos_los_movimientos()
            window["-TABLA-"].update(values=_tabla(movimientos_mostrados))

        if event == "Borrar":
            seleccionados = values["-TABLA-"]
            if seleccionados:
                for indice in seleccionados:
                    gestor.eliminar_movimiento(movimientos_mostrados[indice])
                archivos.guardar_movimientos([m.a_lista() for m in gestor.obtener_todos_los_movimientos()])
                movimientos_mostrados = gestor.obtener_todos_los_movimientos()
                window["-TABLA-"].update(values=_tabla(movimientos_mostrados))
            else:
                sg.popup_error("Error", "Selecciona primero una fila de la tabla para borrarla.")

    window.close()

def _tabla(movimientos):
    filas = []
    for monto, titulo, categoria, tipo, fecha in (m.a_lista() for m in movimientos):
        filas.append([fecha, f"₡{monto}", titulo, categoria, tipo])
    return filas

def _ventana_agregar_categoria():
    layout = [
        [sg.Text("Nombre de la categoría"), sg.Input(key="-NOMBRE-", enable_events=True)],
        [sg.pin(sg.Text(f"Máximo {_MAX_CATEGORIA} caracteres", text_color="red", key="-AVISO_NOMBRE-", visible=False))],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    ventana = sg.Window("Agregar Categoría", layout, modal=True)
    categoria = None

    while True:
        event, values = ventana.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "-NOMBRE-":
            if len(values["-NOMBRE-"]) > _MAX_CATEGORIA:
                ventana["-NOMBRE-"].update(values["-NOMBRE-"][:_MAX_CATEGORIA])
            ventana["-AVISO_NOMBRE-"].update(visible=len(values["-NOMBRE-"]) >= _MAX_CATEGORIA)

        if event == "Guardar":
            nombre = values["-NOMBRE-"].strip()
            if not nombre:
                sg.popup_error("Error", "Debes escribir un nombre de categoría.")
            else:
                categoria = nombre
                break

    ventana.close()
    return categoria

def _ventana_agregar_movimiento(tipo, categorias):
    fecha_hoy = datetime.now().strftime(_FORMATO_FECHA)
    layout = [
        [sg.Text("Título"), sg.Input(key="-TITULO-", enable_events=True)],
        [sg.Text("Monto"), sg.Text("₡"), sg.Input(key="-MONTO-", enable_events=True)],
        [sg.pin(sg.Text(f"Máximo {_MAX_TITULO} caracteres para el título", text_color="red", key="-AVISO_TITULO-", visible=False))],
        [sg.Text("Categoría"), sg.Combo(categorias, key="-CATEGORIA-")],
        [sg.Text("Fecha (dd/mm/yyyy)"), sg.Input(fecha_hoy, key="-FECHA-"), sg.CalendarButton("📅", target="-FECHA-", format=_FORMATO_FECHA, no_titlebar=False)],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]
    ventana = sg.Window(f"Agregar {tipo}", layout, modal=True)
    datos = None
    ultimo_monto_valido = ""

    while True:
        event, values = ventana.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "-TITULO-":
            if len(values["-TITULO-"]) > _MAX_TITULO:
                ventana["-TITULO-"].update(values["-TITULO-"][:_MAX_TITULO])
            ventana["-AVISO_TITULO-"].update(visible=len(values["-TITULO-"]) >= _MAX_TITULO)

        if event == "-MONTO-":
            if _es_monto_parcial_valido(values["-MONTO-"]):
                ultimo_monto_valido = values["-MONTO-"]
            else:
                ventana["-MONTO-"].update(ultimo_monto_valido)

        if event == "Guardar":
            titulo = values["-TITULO-"].strip()
            if not titulo or not values["-MONTO-"] or not values["-CATEGORIA-"] or not values["-FECHA-"]:
                sg.popup_error("Error", "Completa título, monto, categoría y fecha antes de guardar.")
            elif not _es_fecha_valida(values["-FECHA-"]):
                sg.popup_error("Error", "La fecha debe tener el formato dd/mm/yyyy.")
            else:
                try:
                    monto_valido = float(values["-MONTO-"]) > 0
                except ValueError:
                    monto_valido = False
                if not monto_valido:
                    sg.popup_error("Error", "El monto debe ser un número mayor que cero.")
                else:
                    datos = (values["-MONTO-"], titulo, values["-CATEGORIA-"], values["-FECHA-"])
                    break

    ventana.close()
    return datos
