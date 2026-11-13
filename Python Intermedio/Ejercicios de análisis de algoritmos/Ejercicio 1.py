def bubble_sort(list_to_sort): # O(n^2)
    for outer_index in range(len(list_to_sort)): # O(n)
        has_swapped = False
        for inner_index in range(0, len(list_to_sort) - outer_index - 1): # O(n)
            current_element = list_to_sort[inner_index]
            next_element = list_to_sort[inner_index + 1]
            print(f'-- Iteration {outer_index}, {inner_index}. Current element: {current_element}, Next element: {next_element} --')
            if current_element > next_element:
                print(f'-- The current element {current_element} is greater than the next element {next_element}. Swapping them. --')
                list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element # Swap elements
                has_swapped = True
        if not has_swapped:
            return 
my_test_list = [18, 23, 22, 67, 101, 0, 5, 42] # O(1)
bubble_sort(my_test_list)
print(my_test_list)