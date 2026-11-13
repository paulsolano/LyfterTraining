def check_if_lists_have_an_equal(list_a, list_b): # Peor caso: O(n * m), Mejor caso: O(1)
    for element_a in list_a: # O(n)
        for element_b in list_b: # O(m)
            if element_a == element_b:
                return True # si coincide en la primera comparación, aquí se corta todo (mejor caso O(1))

    return False
