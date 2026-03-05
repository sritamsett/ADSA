import random
import math

MIN_RANGE = 10
MAX_RANGE = 999999

class Counter:
    def __init__(self):
        self.time_ops = 0


def binary_search(arr, target, counter):
    low = 0
    high = len(arr) - 1

    while low <= high:
        counter.time_ops += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def complexity_report(counter, n):
    print("\n--- Binary Search COMPLEXITY ANALYSIS ---")
    print("Number of Comparisons:", counter.time_ops)
    print(f"Theoretical Time Complexity: O(log₂ n) = {round(math.log2(n),2)}")



n = int(input("Enter number of elements: "))

print("\nARRAY INPUT METHOD")
print("1. Values from 0 to n-1")
print("2. Random values")

choice = int(input("Enter choice: "))

if choice == 1:
    arr = list(range(n))
else:
    arr = random.sample(range(MIN_RANGE, MAX_RANGE + 1), n)

arr.sort() 

print("\nSorted Array:")
print(arr)

target = int(input("\nEnter element to search: "))

counter = Counter()

index = binary_search(arr, target, counter)

print("\nSearch Result:")
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

complexity_report(counter, n)