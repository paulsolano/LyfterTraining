class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data: 
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)

    def _to_string(self):
        left_part = self.left._to_string() if self.left is not None else ""
        right_part = self.right._to_string() if self.right is not None else ""
        result = str(self.data)
        if left_part != "":
            result = left_part + " -> " + result
        if right_part != "":
            result = result + " -> " + right_part
        return result

    def print_tree(self):
        print(self._to_string())