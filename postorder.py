class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.count += 1

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

def show_complexity(n):
    print("\nTime Complexity: O(n)")
    print(f"Operations ≈ {n}")

# MAIN
bst = BST()

n = int(input("Enter number of elements: "))
for i in range(n):
    bst.insert(int(input()))

print("Postorder Traversal:")
bst.postorder(bst.root)

show_complexity(bst.count)