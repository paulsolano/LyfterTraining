class Node:
    data: str
    next: 'Node'
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack vacío")
            return None
        popped_node = self.top
        self.top = popped_node.next
        return popped_node.data

    def print_stack(self):
        current = self.top
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += " -> "
            current = current.next
        print(result if result else "Stack vacío")