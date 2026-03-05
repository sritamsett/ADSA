from collections import deque
import math

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

def bfs(root, key):
    queue = deque([root])
    steps = 0

    while queue:
        node = queue.popleft()
        steps += 1

        if node.data == key:
            return True, steps

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False, steps

def show_complexity(n):
    print("\nTime Complexity:")
    print("Best Case: O(1)")
    print("Average Case: O(log n)")
    print("Worst Case: O(n)")
    print(f"n = {n}")
    if n > 0:
        print(f"log2(n) = {math.log2(n):.2f}")

# MAIN
bst = BST()

n = int(input("Enter number of elements: "))
for i in range(n):
    bst.insert(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter value to search: "))
found, steps = bfs(bst.root, key)

print("Result:", "Found" if found else "Not Found")
print("Steps:", steps)

show_complexity(bst.count)