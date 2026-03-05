def knapsack():

    n = int(input("Enter number of items: "))

    wt = []
    val = []

    for i in range(n):
        val.append(int(input(f"Enter value of item {i+1}: ")))
        wt.append(int(input(f"Enter weight of item {i+1}: ")))

    W = int(input("Enter knapsack capacity: "))

    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(
                    val[i-1] + dp[i-1][w-wt[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    print("\nSelected Items:")

    selected = [0]*n
    w = W

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected[i-1] = 1
            w -= wt[i-1]

    total_profit = 0
    total_weight = 0

    for i in range(n):
        if selected[i]:
            print(f"Selected item (profit={val[i]}, weight={wt[i]})")
            total_profit += val[i]
            total_weight += wt[i]
        else:
            print(f"Skipped item (profit={val[i]}, weight={wt[i]})")

    print("\nTotal Profit:", total_profit)
    print("Total Weight:", total_weight)


knapsack()