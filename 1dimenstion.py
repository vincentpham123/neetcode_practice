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
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        house1, house2 = 0 ,0 
        # [house1, house2, n, n+1, n+2]
        # the idea is that each number has two decisions
        # we can either add the the house down 2, or just rob the current house 
        
        for n in nums:
            temp = max(n + house1, house2)

            house1 = house2 
            house2 = temp
        
        return house2
class Solution:
    def rob(self, nums: List[int]) -> int:
         return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # the idea is to start from the top and go down
        
        one, two = 1 ,1 

        
        for i in range(n-1, -1,-1):
            temp = one 
            one = two + one 
            two = temp 
        
        return two