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

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # lets think about this

        # we can start from the 1st or 2nd step 

        # we can climb one or two steps 
        # so each step we have the option to add up the i+1, or i +2 
        # we also want the minimum
        # as we take our steps, we should determine what is the minimum 
        # and add as we go on 
        # it is better to start at the end as well 
        # that way we can start grabbing the min out of the choice of 1 or 2 steps

        for i in range(len(cost)-3, -1, -1):
            # this should start us at 3rd from last 

            # we now need to add the costs to the current step 

            cost[i] += min(cost[i+1], cost[i+2])
            # as we go down the steps, we will dynamically update 
        
        return min(cost[0], cost[1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0 ,0 

        for i in nums:

            temp = max(house1+i, house2)
            # house1 and house2 are imaginery houses
            # this allows me to imitate the initial condition
            # house1 represents the orevious house over, and house2 is the previous house
            # house1 + i means that we are robbing the current house along with the previous house over
            # house2 represents stealing the previous house 

            # now we have to update house1 and house2 

            # house1, house2, i, i+1
            
            # we need house1 to be the next house pver
            house1 = house2 
            house2 = temp 
        return house2