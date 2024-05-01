def min_change(amount, coins):
  ans = min_change_helper(amount, coins, {})
  
  if ans == float('inf'):
    return -1 
  else:
    return ans
def min_change_helper(amount, coins, memo):
  # the idea, is that we recursively call
  
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return 0 
  
  if amount < 0:
    return float('inf')
  # we return float cause the coin combination is invalid 
  min_amount = float('inf')
  for coin in coins:
    current_min = 1 + min_change_helper(amount - coin, coins, memo)
    
    min_amount = min(current_min, min_amount)
    
  memo[amount] = min_amount 
  return memo[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        # that is the base case

        for a in range(1, amount + 1):
            # gonna iterate and find the min amount for all these coin amounts basically 

            for i in coins:
                # so i now iterate through the coins and check if they can equal a 

                if a - i >= 0:
                    dp[a] = min(dp[a], 1+ dp[a-i])
                    # the idea is that a - i coins should already been found and is already the min combination from the coins available 
        
        return dp[amount] if dp[amount] != amount +1 else -1