import random

class Counter:
    def __init__(self):
        self.time_ops = 0
        self.comparisons = 0


def bubble_sort(arr, counter):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            counter.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter.time_ops += 1

    return arr


n = int(input("Enter number of elements: "))
case = int(input("1.Best Case  2.Average/Worst Case : "))

if case == 1:
    arr = list(range(n))
    case_name = "Best Case"
else:
    arr = random.sample(range(10, 999999), n)
    case_name = "Average/Worst Case"

counter = Counter()

result = bubble_sort(arr.copy(), counter)

print("\nSorted Array:", result)

print("\nComputational Complexity")
print("Comparisons =", counter.comparisons)
print("Swaps =", counter.time_ops)

theoretical_comparisons = n * (n - 1) // 2

if case == 1:
    theoretical_swaps = 0
else:
    theoretical_swaps = theoretical_comparisons

print("\nTheoretical Complexity")
print("For n =", n)
print("Theoretical Comparisons =", theoretical_comparisons)
print("Theoretical Swaps =", theoretical_swaps)