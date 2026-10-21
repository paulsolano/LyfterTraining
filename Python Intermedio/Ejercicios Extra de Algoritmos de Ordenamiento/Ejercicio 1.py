class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class BubbleSort:
    class Stack:
        def __init__(self):
            self.top = None

        def push(self, data):
            new_node = Node(data, self.top)
            self.top = new_node

        def bubble_sort_push(self, list_to_sort):
            for outer_index in range(len(list_to_sort)):
                for inner_index in range(0, len(list_to_sort) - outer_index - 1):
                    current_element = list_to_sort[inner_index]
                    next_element = list_to_sort[inner_index + 1]

                    if current_element > next_element:
                        list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element

            for element in reversed(list_to_sort):
                self.push(element)

        def pop(self):
            if self.top is None:
                print("Stack vacío")
                return None
            popped_node = self.top
            self.top = popped_node.next
            return popped_node.data

        def bubble_sort_pop(self):
            sorted_list = []
            while self.top is not None:
                sorted_list.append(self.pop())
            return sorted_list

        def print_stack(self):
            current = self.top
            result = ""
            while current is not None:
                result += str(current.data)
                if current.next is not None:
                    result += " -> "
                current = current.next
            print(result if result else "Stack vacío")
