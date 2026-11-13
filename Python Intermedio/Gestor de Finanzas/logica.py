from datetime import datetime

_FORMATO_FECHA = "%d/%m/%Y"

class Movimiento:
    def __init__(self, monto, descripcion, categoria, tipo, fecha):
        self.monto = monto
        self.descripcion = descripcion
        self.categoria = categoria
        self.tipo = tipo
        self.fecha = fecha

    def a_lista(self):
        return [self.monto, self.descripcion, self.categoria, self.tipo, self.fecha]

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.movimientos = []

    def agregar_movimiento(self, movimiento):
        self.movimientos.append(movimiento)

    def obtener_movimientos(self):
        return self.movimientos

class GestorFinanzas:
    def __init__(self):
        self.categorias = {}

    def agregar_categoria(self, nombre):
        if nombre not in self.categorias:
            self.categorias[nombre] = Categoria(nombre)

    def agregar_movimiento(self, monto, descripcion, categoria_nombre, tipo, fecha):
        if categoria_nombre not in self.categorias:
            raise ValueError(f"La categoría '{categoria_nombre}' no existe")
        movimiento = Movimiento(monto, descripcion, categoria_nombre, tipo, fecha)
        self.categorias[categoria_nombre].agregar_movimiento(movimiento)

    def obtener_movimientos_por_categoria(self, categoria_nombre):
        if categoria_nombre in self.categorias:
            return self.categorias[categoria_nombre].obtener_movimientos()
        return []

    def obtener_categorias(self):
        return list(self.categorias.keys())

    def obtener_todos_los_movimientos(self):
        todos = []
        for categoria in self.categorias.values():
            todos.extend(categoria.obtener_movimientos())
        return todos

    def eliminar_movimiento(self, movimiento):
        categoria = self.categorias.get(movimiento.categoria)
        if categoria is not None and movimiento in categoria.movimientos:
            categoria.movimientos.remove(movimiento)

    def obtener_movimientos_en_rango(self, fecha_inicio, fecha_fin):
        inicio = datetime.strptime(fecha_inicio, _FORMATO_FECHA)
        fin = datetime.strptime(fecha_fin, _FORMATO_FECHA)
        resultado = []
        for movimiento in self.obtener_todos_los_movimientos():
            fecha_movimiento = datetime.strptime(movimiento.fecha, _FORMATO_FECHA)
            if inicio <= fecha_movimiento <= fin:
                resultado.append(movimiento)
        return resultado
