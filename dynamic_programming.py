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
