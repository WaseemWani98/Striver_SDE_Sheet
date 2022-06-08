"""
BEST TIME TO BUY AND SELL STOCK
--------------------------------------------------
You are given an array/list 'prices' where the elements of the array represent
the prices of the stock as they were yesterday and indices of the array represent
minutes. Your task is to find and return the maximum profit you can make by buying
and selling the stock. You can buy and sell the stock only once.
"""

#   Approach #1 :
#   Brute-Force Approach would be to check profit for every element
#   and store the max profit in each case.

#   T.C : O(N^2)
#   S.C : O(1)
import sys


def max_profit1(prices):
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
    return max_profit


#   Approach #2 :
#   Optimised Approach would be to linearly traverse the array
#   and keep a track of minimal element on the left side.
#   Initially max_profit will be zero and min will be set to +inf
#   As we move forward, we compare it with min and if its lesser
#   we update min. Otherwise, we calculate profit and set max_profit
#   to max of profit and max_profit

#   T.C : O(N)
#   S.C : O(1)


def max_profit2(prices):
    max_profit = 0
    min_price = sys.maxsize
    for i in prices:
        if i < min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit

print(max_profit2([7,1,5,3,6,4]))
