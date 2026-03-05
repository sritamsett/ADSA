import random

class Counter:
    def __init__(self):
        self.time_ops = 0
        self.comparisons = 0


def insertion_sort(arr, counter):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            counter.comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                counter.time_ops += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
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

result = insertion_sort(arr.copy(), counter)

print("\nSorted Array:", result)

print("\nComputational Complexity")
print("Comparisons =", counter.comparisons)
print("Shifts =", counter.time_ops)

if case == 1:
    theoretical_comparisons = n - 1
    theoretical_shifts = 0
else:
    theoretical_comparisons = n * (n - 1) // 2
    theoretical_shifts = n * (n - 1) // 2

print("\nTheoretical Complexity")
print("For n =", n)
print("Theoretical Comparisons =", theoretical_comparisons)
print("Theoretical Shifts =", theoretical_shifts)