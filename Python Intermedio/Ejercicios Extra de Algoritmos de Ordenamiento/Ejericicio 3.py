class BubbleSortBinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _bubble_sort(self, list_to_sort):
            for outer_index in range(len(list_to_sort)):
                for inner_index in range(0, len(list_to_sort) - outer_index - 1):
                    current_element = list_to_sort[inner_index]
                    next_element = list_to_sort[inner_index + 1]
    
                    if current_element > next_element:
                        list_to_sort[inner_index], list_to_sort[inner_index + 1] = next_element, current_element

    def bubble_sort_insert(self, list_to_sort):
        self._bubble_sort(list_to_sort)
        for element in list_to_sort:
            self.insert(element)
        return self
    def insert(self, data):
        if self.data:
            if data < self.data: 
                if self.left is None:
                    self.left = BubbleSortBinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BubbleSortBinaryTree(data)
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