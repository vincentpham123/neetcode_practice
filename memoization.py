class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self._coinChange(coins, amount, {})

        if result == float('inf'):
            return -1
        else:
            return result
    
    def _coinChange(self, coins, amount,memo):

        if amount in memo:
            return memo[amount]
        
        if amount == 0:
            # that means there is a solution
            return 0 
        
        if amount < 0:
            return float('inf')
        
        # now that i have my basecases, 
        minchange = float('inf')
        for i in coins:
            # i now need to iterate through the coins

            temp_min = 1 + self._coinChange(coins, amount-i,memo)

            # temp_min should either equal a number or float 
            minchange = min(temp_min, minchange)
        
        memo[amount] = minchange

        return memo[amount]