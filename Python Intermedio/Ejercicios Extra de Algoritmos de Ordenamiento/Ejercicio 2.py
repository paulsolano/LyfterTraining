class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

class BubbleSortDeque: # Implementación del algoritmo de ordenamiento burbuja utilizando una cola doble
    def __init__(self):
        self.head = None
        self.tail = None

    def _bubble_sort(self, list_to_sort):
        for outer_index in range(len(list_to_sort)):
            for inner_index in range(0, len(list_to_sort) - outer_index - 1):
                current_element = list_to_sort[inner_index]
                next_element = list_to_sort[inner_index + 1]

                if current_element > next_element:
                    list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element

    def bubble_sort_push_left(self, list_to_sort):
        self._bubble_sort(list_to_sort)
        for element in reversed(list_to_sort):
            self.push_left(element)

    def bubble_sort_push_right(self, list_to_sort):
        self._bubble_sort(list_to_sort)
        for element in list_to_sort:
            self.push_right(element)

    def bubble_sort_pop_left(self):
        sorted_list = []
        while self.head is not None:
            sorted_list.append(self.pop_left())
        return sorted_list

    def bubble_sort_pop_right(self):
        sorted_list = []
        while self.tail is not None:
            sorted_list.append(self.pop_right())
        return sorted_list

    def push_left(self, data):
        new_node = Node(data, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def push_right(self, data):
        new_node = Node(data, self.tail, None)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def pop_left(self):
        if self.head is None:
            print("Deque vacío")
            return None
        popped_node = self.head
        self.head = popped_node.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return popped_node.data

    def pop_right(self):
        if self.tail is None:
            print("Deque vacío")
            return None
        popped_node = self.tail
        self.tail = popped_node.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return popped_node.data

    def print_deque(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += " <-> "
            current = current.next
        print(result if result else "Deque vacío")