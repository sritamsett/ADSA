import random
import math

MIN_RANGE = 10
MAX_RANGE = 999999

class Counter:
    def __init__(self):
        self.time_ops = 0


def linear_search(arr, target, counter):
    for i in range(len(arr)):
        counter.time_ops += 1
        if arr[i] == target:
            return i
    return -1


def complexity_report(counter, n):
    print("\n--- Linear Search COMPLEXITY ANALYSIS ---")
    print("Number of Comparisons:", counter.time_ops)
    print(f"Theoretical Time Complexity: O(n) = {n}")


n = int(input("Enter number of elements: "))

print("\nARRAY INPUT METHOD")
print("1. Values from 0 to n-1")
print("2. Random values")

choice = int(input("Enter choice: "))

if choice == 1:
    arr = list(range(n))
else:
    arr = random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)

print("\nArray:")
print(arr)

target = int(input("\nEnter element to search: "))

counter = Counter()

index = linear_search(arr, target, counter)

print("\nSearch Result:")
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

complexity_report(counter, n)