def validated_bubble_sort(list_to_sort):
    def validate_list(list_to_sort): # Función para validar la lista
        if not isinstance(list_to_sort, list):
            raise ValueError("La entrada debe ser una lista.")
        if len(list_to_sort) == 0:
            raise ValueError("Error: La lista está vacía")
        for element in list_to_sort:
            if not isinstance(element, (int, float)):
                raise ValueError("Error: La lista contiene elementos no numéricos")
    validate_list(list_to_sort)
    for outer_index in range(len(list_to_sort)):
        has_swapped = False
        for inner_index in range(0, len(list_to_sort) - outer_index - 1):
            current_element = list_to_sort[inner_index]
            next_element = list_to_sort[inner_index + 1]
            print(f'-- Iteration {outer_index}, {inner_index}. Current element: {current_element}, Next element: {next_element} --')
            if current_element > next_element:
                print(f'-- The current element {current_element} is greater than the next element {next_element}. Swapping them. --')
                list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element # Swap elements
                has_swapped = True
        if not has_swapped:
            return
my_test_list = [18, 23, 22, 4, "hola", 0, 5, 42]
try:
    validated_bubble_sort(my_test_list)
    print(my_test_list)
except ValueError as e:
    print(e)
