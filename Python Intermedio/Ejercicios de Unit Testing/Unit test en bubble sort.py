def bubble_sort(list_to_sort, verbose=False):
    if not isinstance(list_to_sort, list):
        raise TypeError("bubble_sort espera una lista como parámetro")
    for outer_index in range(len(list_to_sort)):
        has_swapped = False
        for inner_index in range(0, len(list_to_sort) - outer_index - 1):
            current_element = list_to_sort[inner_index]
            next_element = list_to_sort[inner_index + 1]
            if verbose:
                print(f'-- Iteration {outer_index}, {inner_index}. Current element: {current_element}, Next element: {next_element} --')
            if current_element > next_element:
                if verbose:
                    print(f'-- The current element {current_element} is greater than the next element {next_element}. Swapping them. --')
                list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element # Swap elements
                has_swapped = True
        if not has_swapped:
            return
my_test_list = [18, 23, 22, 67, 101, 0, 5, 42]
bubble_sort(my_test_list, verbose=True)
print(my_test_list)

def test_bubble_sort_works_with_small_list():
    test_list = [3, 1, 2]
    bubble_sort(test_list)
    assert test_list == [1, 2, 3], f"Expected [1, 2, 3], but got {test_list}"

def test_bubble_sort_works_with_large_list():
    test_list = list(range(150, 0, -1))
    bubble_sort(test_list)
    assert test_list == list(range(1, 151)), f"Expected a sorted list from 1 to 150, but got {test_list}"

def test_bubble_sort_works_with_empty_list():
    test_list = []
    bubble_sort(test_list)
    assert test_list == [], f"Expected [], but got {test_list}"

def test_bubble_sort_works_with_single_element_list():
    test_list = [1]
    bubble_sort(test_list)
    assert test_list == [1], f"Expected [1], but got {test_list}"

def test_bubble_sort_fails_with_non_list_param():
    try:
        bubble_sort("no soy una lista")
        assert False, "Se esperaba un TypeError, pero no ocurrió"
    except TypeError:
        pass