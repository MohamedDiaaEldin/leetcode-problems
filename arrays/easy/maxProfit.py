'''
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
## enhancement for v2
def maxProfit( prices):

    left , right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right] : 
            max_profit = max(prices[right] - prices[left], max_profit) 
        else : 
            left = right 
        right += 1
    return max_profit 

# time o(n)
# space o(1)
def maxProfit_v2( prices):
    left, right = 0 , 1        
    max = 0
    
    while right < len(prices): 
        if prices[right] < prices[left]  : 
            left = right
        elif prices[right] - prices[left] > max: 
            max = prices[right] - prices[left]
            day = right 
        right += 1 
    return max


## brute force approach 
## time o(n^2)
## space o(1)
def maxProfit_v1( prices):
    left, right = 0 , len(prices) -1 
    min = prices[left]
    max = prices[right]
    while left < right : 
        if prices[left] <= min  :
            min = prices[left]
            left += 1
        if prices[right] >= max : 
            max = prices[right]
            right -=1 
    return max
    
nums = [7,1,5,3,6,4]

print(maxProfit(nums))