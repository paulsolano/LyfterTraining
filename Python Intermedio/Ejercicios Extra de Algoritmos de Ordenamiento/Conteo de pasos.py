def bubble_sort_steps(list_to_sort):
    global interchanges
    global iterator
    for outer_index in range(len(list_to_sort)):
        has_swapped = False
        for inner_index in range(0, len(list_to_sort) - outer_index - 1):
            current_element = list_to_sort[inner_index]
            next_element = list_to_sort[inner_index + 1]
            iterator = outer_index + 1 
            print(f'-- Iteration {outer_index}, {inner_index}. Current element: {current_element}, Next element: {next_element} --')
            if current_element > next_element:
                print(f'-- The current element {current_element} is greater than the next element {next_element}. Swapping them. --')
                list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element # Swap elements
                has_swapped = True
                interchanges += 1
        if not has_swapped:
            return  # If no swaps were made, the list is sorted and we can exit
my_test_list = [18, 23, 22, 67, 93, 49, 11,101, 0, 5, 42]
interchanges = 0
iterator = 0
bubble_sort_steps(my_test_list)
print(my_test_list)
print(f'Total iterations made: {iterator}')
print(f'Total interchanges made: {interchanges}')