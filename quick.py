import random
import sys
import math

sys.setrecursionlimit(10**7)

class Counter:
    def __init__(self):
        self.time_ops = 0
        self.comparisons = 0


def partition(arr, low, high, counter):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        counter.comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            counter.time_ops += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    counter.time_ops += 1
    return i + 1


def quick_sort(arr, low, high, counter):
    if low < high:
        pi = partition(arr, low, high, counter)
        quick_sort(arr, low, pi - 1, counter)
        quick_sort(arr, pi + 1, high, counter)


n = int(input("Enter number of elements: "))
case = int(input("1.Worst Case  2.Best/Average Case : "))

if case == 1:
    arr = list(range(n))
    case_name = "Worst Case"
else:
    arr = random.sample(range(10, 999999), n)
    case_name = "Best/Average Case"

counter = Counter()

result = arr.copy()
quick_sort(result, 0, n - 1, counter)

print("\nSorted Array:", result)

print("\nComputational Complexity")
print("Comparisons =", counter.comparisons)
print("Swaps =", counter.time_ops)

if case == 1:
    theoretical_operations = n * (n - 1) // 2
else:
    theoretical_operations = int(n * math.log2(n)) if n > 0 else 0

print("\nTheoretical Complexity")
print("For n =", n)
print("Theoretical Operations ≈", theoretical_operations)