from datetime import datetime

import validations

class Movement:
    def __init__(self, amount, title, category, movement_type, date):
        if not validations.is_valid_amount(amount):
            raise ValueError("El monto debe ser un número mayor que cero")
        if not validations.is_valid_text(title):
            raise ValueError("El título no puede estar vacío")
        if not validations.is_valid_date(date):
            raise ValueError("La fecha debe tener el formato dd/mm/yyyy")
        if not validations.is_not_future_date(date):
            raise ValueError("La fecha no puede ser una fecha futura")
        self.amount = float(amount)
        self.title = title
        self.category = category
        self.movement_type = movement_type
        self.date = date

    def to_dict(self):
        return {
            "monto": self.amount,
            "titulo": self.title,
            "categoria": self.category,
            "tipo": self.movement_type,
            "fecha": self.date,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["monto"], data["titulo"], data["categoria"], data["tipo"], data["fecha"])

class Category:
    def __init__(self, name):
        self.name = name
        self.movements = []

    def add_movement(self, movement):
        self.movements.append(movement)

    def get_movements(self):
        return self.movements

class FinanceManager:
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        if name not in self.categories:
            self.categories[name] = Category(name)

    def add_movement(self, amount, title, category_name, movement_type, date):
        if category_name not in self.categories:
            raise ValueError(f"La categoría '{category_name}' no existe")
        movement = Movement(amount, title, category_name, movement_type, date)
        self.categories[category_name].add_movement(movement)

    def get_movements_by_category(self, category_name):
        if category_name in self.categories:
            return self.categories[category_name].get_movements()
        return []

    def get_categories(self):
        return list(self.categories.keys())

    def get_all_movements(self):
        all_movements = []
        for category in self.categories.values():
            all_movements.extend(category.get_movements())
        return all_movements

    def remove_movement(self, movement):
        category = self.categories.get(movement.category)
        if category is not None and movement in category.movements:
            category.movements.remove(movement)

    def get_movements_in_range(self, start_date, end_date):
        start = datetime.strptime(start_date, validations.DATE_FORMAT)
        end = datetime.strptime(end_date, validations.DATE_FORMAT)
        if start > end:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin")
        result = []
        for movement in self.get_all_movements():
            movement_date = datetime.strptime(movement.date, validations.DATE_FORMAT)
            if start <= movement_date <= end:
                result.append(movement)
        return result

    def calculate_balance(self):
        balance = 0.0
        for movement in self.get_all_movements():
            if movement.movement_type == "Ingreso":
                balance += movement.amount
            else:
                balance -= movement.amount
        return balance
