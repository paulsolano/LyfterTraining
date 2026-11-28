def suma(a, b):
    return a + b

def promedio(numeros):
    return sum(numeros) / len(numeros)

def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

class TestOperacionesNumericas:
    def test_con_numeros_positivos(self):
        assert suma(2, 3) == 5
        assert promedio([2, 4, 6]) == 4
        assert celsius_a_fahrenheit(100) == 212

    def test_con_numeros_negativos(self):
        assert suma(-2, -3) == -5
        assert promedio([-2, -4, -6]) == -4
        assert celsius_a_fahrenheit(-40) == -40

    def test_con_ceros(self):
        assert suma(0, 0) == 0
        assert promedio([0, 0, 0]) == 0
        assert celsius_a_fahrenheit(0) == 32
