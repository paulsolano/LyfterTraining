class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

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