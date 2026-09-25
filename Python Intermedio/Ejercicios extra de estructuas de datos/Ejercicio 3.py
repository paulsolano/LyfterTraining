class DoubleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else: 
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def print_forward(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += " -> "
            current = current.next
        print(result if result else "Lista vacía")

    def print_backward(self):
        current = self.tail
        result = ""
        while current is not None:
            result += str(current.data)
            if current.prev is not None:
                result += " -> "
            current = current.prev
        print(result if result else "Lista vacía")
