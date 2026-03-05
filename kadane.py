def kadane():

    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    max_so_far = arr[0]
    curr_max = arr[0]

    start = end = temp_start = 0

    for i in range(1, n):
        if arr[i] > curr_max + arr[i]:
            curr_max = arr[i]
            temp_start = i
        else:
            curr_max += arr[i]

        if curr_max > max_so_far:
            max_so_far = curr_max
            start = temp_start
            end = i

    print("\nMaximum Subarray Sum =", max_so_far)
    print("Maximum Subarray =", arr[start:end+1])


kadane()