"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amount:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        if dp[-1] == float("inf"):
            return -1
        return dp[-1]