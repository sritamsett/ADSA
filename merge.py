import random
import math

class Counter:
    def __init__(self):
        self.time_ops = 0
        self.comparisons = 0


def merge(left, right, counter):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        counter.comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            counter.time_ops += 1
            i += 1
        else:
            result.append(right[j])
            counter.time_ops += 1
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr, counter):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)

    return merge(left, right, counter)


n = int(input("Enter number of elements: "))

arr = random.sample(range(10, 999999), n)

counter = Counter()

result = merge_sort(arr.copy(), counter)

print("\nSorted Array:", result)

print("\nComputational Complexity")
print("Comparisons =", counter.comparisons)
print("Operations =", counter.time_ops)

theoretical_operations = int(n * math.log2(n)) if n > 0 else 0

print("\nTheoretical Complexity")
print("For n =", n)
print("Theoretical Operations ≈", theoretical_operations)