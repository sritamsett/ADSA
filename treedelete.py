class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            # Node found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._min_value(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)

        return root

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# MAIN
bst = BST()

n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    bst.insert(val)

print("Before Deletion:")
bst.inorder(bst.root)

key = int(input("\nEnter value to delete: "))
bst.delete(key)

print("After Deletion:")
bst.inorder(bst.root)