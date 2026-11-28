class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class Basic_queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, add_item):
        if add_item is None:
            print("No se puede agregar un elemento nulo a la cola")
            return
        new_node = Node(add_item)
        if self.tail is not None:
            self.tail.next_node = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            print("Cola vacía")
            return None
        else:
            dequeued_node = self.head
            self.head = dequeued_node.next_node
            if self.head is None:
                self.tail = None
            self.size -= 1
            return dequeued_node.data

    def print_all(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next_node is not None:
                result += " -> "
            current = current.next_node
        print(result if result else "Cola vacía")

    def is_empty(self):
        return self.size == 0
