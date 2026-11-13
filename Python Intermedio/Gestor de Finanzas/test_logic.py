from datetime import datetime, timedelta

import pytest

import logic
import validations

class TestMovement:
    def test_to_dict_returns_data_with_its_keys(self):
        movement = logic.Movement("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        assert movement.to_dict() == {
            "monto": 150.50,
            "titulo": "Super",
            "categoria": "Comida",
            "tipo": "Gasto",
            "fecha": "02/07/2025",
        }

    def test_from_dict_rebuilds_the_movement(self):
        data = {
            "monto": "150.50",
            "titulo": "Super",
            "categoria": "Comida",
            "tipo": "Gasto",
            "fecha": "02/07/2025",
        }
        movement = logic.Movement.from_dict(data)
        assert movement.to_dict() == {
            "monto": 150.50,
            "titulo": "Super",
            "categoria": "Comida",
            "tipo": "Gasto",
            "fecha": "02/07/2025",
        }

    def test_negative_amount_raises_error(self):
        with pytest.raises(ValueError):
            logic.Movement("-150.50", "Super", "Comida", "Gasto", "02/07/2025")

    def test_zero_amount_raises_error(self):
        with pytest.raises(ValueError):
            logic.Movement("0", "Super", "Comida", "Gasto", "02/07/2025")

    def test_date_with_wrong_format_raises_error(self):
        with pytest.raises(ValueError):
            logic.Movement("150.50", "Super", "Comida", "Gasto", "2025-07-02")

    def test_empty_title_raises_error(self):
        with pytest.raises(ValueError):
            logic.Movement("150.50", "   ", "Comida", "Gasto", "02/07/2025")

    def test_future_date_raises_error(self):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime(validations.DATE_FORMAT)
        with pytest.raises(ValueError):
            logic.Movement("150.50", "Super", "Comida", "Gasto", tomorrow)

class TestFinanceManager:
    def test_add_category_makes_it_available(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        assert manager.get_categories() == ["Comida"]

    def test_duplicate_category_does_not_create_another(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        manager.add_category("Comida")
        assert manager.get_categories() == ["Comida"]

    def test_add_movement_without_existing_category_raises_error(self):
        manager = logic.FinanceManager()
        with pytest.raises(ValueError):
            manager.add_movement("150.50", "Super", "Comida", "Gasto", "02/07/2025")

    def test_add_movement_with_negative_amount_raises_error(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        with pytest.raises(ValueError):
            manager.add_movement("-150.50", "Super", "Comida", "Gasto", "02/07/2025")

    def test_add_movement_with_invalid_date_raises_error(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        with pytest.raises(ValueError):
            manager.add_movement("150.50", "Super", "Comida", "Gasto", "02-07-2025")

    def test_add_movement_associates_it_with_its_category(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        manager.add_movement("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        movements = manager.get_movements_by_category("Comida")
        assert len(movements) == 1
        assert movements[0].to_dict() == {
            "monto": 150.50,
            "titulo": "Super",
            "categoria": "Comida",
            "tipo": "Gasto",
            "fecha": "02/07/2025",
        }

    def test_get_movements_by_nonexistent_category_returns_empty_list(self):
        manager = logic.FinanceManager()
        assert manager.get_movements_by_category("Comida") == []

    def test_get_all_movements_joins_several_categories(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        manager.add_category("Trabajo")
        manager.add_movement("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        manager.add_movement("2000", "Salario", "Trabajo", "Ingreso", "01/07/2025")
        all_movements = [m.to_dict() for m in manager.get_all_movements()]
        assert all_movements == [
            {"monto": 150.50, "titulo": "Super", "categoria": "Comida", "tipo": "Gasto", "fecha": "02/07/2025"},
            {"monto": 2000.0, "titulo": "Salario", "categoria": "Trabajo", "tipo": "Ingreso", "fecha": "01/07/2025"},
        ]

    def test_remove_movement_takes_it_out_of_its_category(self):
        manager = logic.FinanceManager()
        manager.add_category("Comida")
        manager.add_movement("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        movement = manager.get_all_movements()[0]
        manager.remove_movement(movement)
        assert manager.get_all_movements() == []

    def test_get_movements_in_range_filters_by_date(self):
        manager = logic.FinanceManager()
        manager.add_category("Trabajo")
        manager.add_category("Comida")
        manager.add_category("Ropa")
        manager.add_movement("1000", "Salario", "Trabajo", "Ingreso", "02/07/2025")
        manager.add_movement("20", "Comida", "Comida", "Gasto", "03/07/2025")
        manager.add_movement("50", "Ropa", "Ropa", "Gasto", "12/07/2025")
        result = manager.get_movements_in_range("01/07/2025", "10/07/2025")
        assert [m.title for m in result] == ["Salario", "Comida"]

    def test_get_movements_in_range_includes_the_limits(self):
        manager = logic.FinanceManager()
        manager.add_category("Trabajo")
        manager.add_category("Ropa")
        manager.add_movement("1000", "Salario", "Trabajo", "Ingreso", "01/07/2025")
        manager.add_movement("50", "Ropa", "Ropa", "Gasto", "10/07/2025")
        result = manager.get_movements_in_range("01/07/2025", "10/07/2025")
        assert [m.title for m in result] == ["Salario", "Ropa"]

    def test_get_movements_in_range_with_start_after_end_raises_error(self):
        manager = logic.FinanceManager()
        with pytest.raises(ValueError):
            manager.get_movements_in_range("10/07/2025", "01/07/2025")

    def test_calculate_balance_adds_income_and_subtracts_expenses(self):
        manager = logic.FinanceManager()
        manager.add_category("Trabajo")
        manager.add_category("Comida")
        manager.add_movement("1000", "Salario", "Trabajo", "Ingreso", "01/07/2025")
        manager.add_movement("150.50", "Super", "Comida", "Gasto", "02/07/2025")
        assert manager.calculate_balance() == 849.50

    def test_calculate_balance_with_no_movements_is_zero(self):
        manager = logic.FinanceManager()
        assert manager.calculate_balance() == 0.0
