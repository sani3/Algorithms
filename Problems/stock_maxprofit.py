def stock_max_profit_bruteforce(prices):
    """(list) -> number

    Returns the maximum possible profit for a list of stock prices
    """

    price_index = range(len(prices))
    max_profit = prices[1] - prices[0]

    # For each price at buy_index
    #   For each sell_index above the current buy_index
    #       compute profit
    #       update max_profit if profit is greater than current max_profit
    for buy_index in price_index:
        for sell_index in price_index[buy_index + 1:]:
            profit = prices[sell_index] - prices[buy_index]
            max_profit = max(max_profit, profit)
    return max_profit


def stock_max_profit(prices):
    """(list) -> number

    Returns the maximum possible profit for a list of stock prices
    """

    max_profit = prices[1] - prices[0]

    # For each buy_index
    #   Compute maximum sell_price of all sell_prices current buy_index
    #   Compute profit
    #   Update max_profit if profit is greater than current max_profit
    for buy_index in range(len(prices) - 1):
        max_sell_price = max(prices[buy_index + 1:])
        profit = max_sell_price - prices[buy_index]
        max_profit = max(max_profit, profit)
    return max_profit


if __name__ == 'main':
    import unittest

    class MaxTest(unittest.TestCase):
        def test_stock_max_profit_bruteforce_1(self):
            self.assertEqual(stock_max_profit_bruteforce([3, 2, 4, 5, 6, 8, 26, 7]), 24)

        def test_stock_max_profit_bruteforce_2(self):
            self.assertEqual(stock_max_profit_bruteforce([26, 8, 7, 6, 5, 4, 3, 2]), -1)

        def test_stock_max_profit_1(self):
            self.assertEqual(stock_max_profit([3, 2, 4, 5, 6, 8, 26, 7]), 24)

        def test_stock_max_profit_2(self):
            self.assertEqual(stock_max_profit([26, 8, 7, 6, 5, 4, 3, 2]), -1)
