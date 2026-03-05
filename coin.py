def coin_change():

    print("\n=== COIN CHANGE PROBLEM ===")

    n = int(input("Enter number of coin denominations: "))
    coins = []

    for i in range(n):
        coin = int(input(f"Enter denomination {i+1}: "))
        coins.append(coin)


    coins.sort(reverse=True)

    amount = int(input("Enter amount to change: "))

    result = {}
    remaining = amount


    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            remaining -= coin * count
            result[coin] = count

    print("\nCoins Used:")
    for coin, count in result.items():
        print(f"{coin} -> {count} times")

    if remaining != 0:
        print("Remaining amount cannot be changed using given coins.")
    else:
        print("Change completed successfully.")


coin_change()