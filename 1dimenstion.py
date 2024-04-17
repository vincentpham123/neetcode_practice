class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        for i in range(n-1):
            temp = one 

            one = one + two 
            two = temp 
            # adding up all steps as we reach the end 
        return one

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        for i in range(len(cost)-3, -1, -1):
            # need to go backwards and start at the 3rd to last 

            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])