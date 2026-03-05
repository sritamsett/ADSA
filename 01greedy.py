def greedy_knapsack():

    print("\n=== GREEDY 0/1 KNAPSACK ===")

    n = int(input("Enter number of items: "))

    profit = []
    weight = []
    ratio = []

    for i in range(n):
        p = float(input(f"Enter profit of item {i+1}: "))
        w = float(input(f"Enter weight of item {i+1}: "))
        profit.append(p)
        weight.append(w)
        ratio.append(p / w)

    W = float(input("Enter knapsack capacity: "))


    items = list(zip(profit, weight, ratio))
    items.sort(key=lambda x: x[2], reverse=True)

    totalProfit = 0
    currentWeight = 0

    print("\nSelected Items:")

    for p, w, r in items:
        if currentWeight + w <= W:
            currentWeight += w
            totalProfit += p
            print(f"Selected item (profit={p}, weight={w}, ratio={r:.2f})")
        else:
            print(f"Skipped item (profit={p}, weight={w}, ratio={r:.2f})")

    print("\nTotal Profit:", totalProfit)
    print("Total Weight:", currentWeight)



greedy_knapsack()