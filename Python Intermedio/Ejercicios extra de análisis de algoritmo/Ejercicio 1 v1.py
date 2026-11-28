def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def add_formula(n):
    return n * (n + 1) // 2


# Análisis de complejidad:
#
# Versión 1 (manual_add): O(n). El ciclo for itera n veces y en cada vuelta
# hace una suma, así que el tiempo crece de forma lineal con n.
#
# Versión 2 (add_formula): O(1). Es una sola fórmula matemática (una
# multiplicación, una suma y una división), sin importar qué tan grande sea n.
#
# Con n = 1.000.000.000 elegiría la versión 2 (add_formula): hace 3 operaciones
# en vez de mil millones de iteraciones, y da el mismo resultado.
