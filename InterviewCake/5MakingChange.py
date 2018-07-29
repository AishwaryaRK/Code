def change_possibilities(amount, denominations):
    ways_of_making_n_cents = [0] * (amount + 1)
    ways_of_making_n_cents[0] = 1
    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            ways_of_making_n_cents[higher_amount] += ways_of_making_n_cents[higher_amount - coin]
            print(coin, higher_amount, ways_of_making_n_cents)
    print(ways_of_making_n_cents)
    return ways_of_making_n_cents[amount]


print(change_possibilities(4, [1, 2, 3, 4]))
