"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.
"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amt in range(1, amount + 1):
                if coin <= amt:
                    dp[amt] += dp[amt - coin]

        return dp[-1]
