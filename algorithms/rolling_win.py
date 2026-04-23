prices = [7, 1, 5, 3, 6, 4]

def maxProfit(prices):
    left = 0
    right =1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            if max_profit < current_profit:
                max_profit = current_profit
        else:
            left = right 
        right += 1
    return max_profit

maxProfit([7, 1, 5, 3, 6, 4, 0.5, 10])
maxProfit(prices = [5, 4, 3, 2, 1])
