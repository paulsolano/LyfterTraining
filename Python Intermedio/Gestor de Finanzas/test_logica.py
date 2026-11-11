import logica

class TestMovimiento:
    def test_a_lista_devuelve_los_datos_en_orden(self):
        movimiento = logica.Movimiento("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        assert movimiento.a_lista() == ["150.50", "Super", "Comida", "Gasto", "02/07/2025"]

class TestGestorFinanzas:
    def test_agregar_categoria_la_deja_disponible(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_categoria("Comida")
        assert gestor.obtener_categorias() == ["Comida"]

    def test_agregar_categoria_duplicada_no_crea_otra(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_categoria("Comida")
        gestor.agregar_categoria("Comida")
        assert gestor.obtener_categorias() == ["Comida"]

    def test_agregar_movimiento_crea_la_categoria_si_no_existe(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_movimiento("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        assert gestor.obtener_categorias() == ["Comida"]

    def test_agregar_movimiento_lo_asocia_a_su_categoria(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_movimiento("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        movimientos = gestor.obtener_movimientos_por_categoria("Comida")
        assert len(movimientos) == 1
        assert movimientos[0].a_lista() == ["150.50", "Super", "Comida", "Gasto", "02/07/2025"]

    def test_obtener_movimientos_por_categoria_inexistente_devuelve_lista_vacia(self):
        gestor = logica.GestorFinanzas()
        assert gestor.obtener_movimientos_por_categoria("Comida") == []

    def test_obtener_todos_los_movimientos_junta_varias_categorias(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_movimiento("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        gestor.agregar_movimiento("2000", "Salario", "Trabajo", "Ingreso", "01/07/2025")
        todos = [m.a_lista() for m in gestor.obtener_todos_los_movimientos()]
        assert todos == [
            ["150.50", "Super", "Comida", "Gasto", "02/07/2025"],
            ["2000", "Salario", "Trabajo", "Ingreso", "01/07/2025"],
        ]

    def test_eliminar_movimiento_lo_quita_de_su_categoria(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_movimiento("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        movimiento = gestor.obtener_todos_los_movimientos()[0]
        gestor.eliminar_movimiento(movimiento)
        assert gestor.obtener_todos_los_movimientos() == []

    def test_obtener_movimientos_en_rango_filtra_por_fecha(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_movimiento("1000", "Salario", "Trabajo", "Ingreso", "02/07/2025")
        gestor.agregar_movimiento("20", "Comida", "Comida", "Gasto", "03/07/2025")
        gestor.agregar_movimiento("50", "Ropa", "Ropa", "Gasto", "12/07/2025")
        resultado = gestor.obtener_movimientos_en_rango("01/07/2025", "10/07/2025")
        assert [m.descripcion for m in resultado] == ["Salario", "Comida"]

    def test_obtener_movimientos_en_rango_incluye_los_limites(self):
        gestor = logica.GestorFinanzas()
        gestor.agregar_movimiento("1000", "Salario", "Trabajo", "Ingreso", "01/07/2025")
        gestor.agregar_movimiento("50", "Ropa", "Ropa", "Gasto", "10/07/2025")
        resultado = gestor.obtener_movimientos_en_rango("01/07/2025", "10/07/2025")
        assert [m.descripcion for m in resultado] == ["Salario", "Ropa"]
