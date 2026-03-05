import random

class Counter:
    def __init__(self):
        self.time_ops = 0
        self.comparisons = 0


def selection_sort(arr, counter):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            counter.comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        counter.time_ops += 1

    return arr


n = int(input("Enter number of elements: "))

arr = random.sample(range(10, 999999), n)

counter = Counter()

result = selection_sort(arr.copy(), counter)

print("\nSorted Array:", result)

print("\nComputational Complexity")
print("Comparisons =", counter.comparisons)
print("Swaps =", counter.time_ops)

theoretical_comparisons = n * (n - 1) // 2
theoretical_swaps = n

print("\nTheoretical Complexity")
print("For n =", n)
print("Theoretical Comparisons =", theoretical_comparisons)
print("Theoretical Swaps =", theoretical_swaps)