def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2

class TestDivision:
    def test_divide_con_numeros_positivos(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3

    def test_divide_por_cero(self):
        try:
            divide(10, 0)
            assert False, "Se esperaba un ValueError, pero no ocurrió"
        except ValueError:
            pass

    def test_divide_con_un_string(self):
        try:
            divide(10,"2")
            assert False, "Se esperaba un TypeError, pero no ocurrió"
        except TypeError:
            pass


