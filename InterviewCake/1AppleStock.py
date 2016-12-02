def compute_best_profit(stock_prices_yesterday):
    best_profit = 0
    min_price = None
    for price in stock_prices_yesterday:
        if min_price == None or price < min_price:
            min_price = price
        if price - min_price > best_profit:
            best_profit = price - min_price
    return best_profit
