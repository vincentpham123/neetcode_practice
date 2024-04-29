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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i ,i
            # starting at the current index

            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1 
                r += 1

                # starting from the middle and blooming out 
            
            # even length 

            l, r = i , i+1 
            # adding 1 to account for even length substrings
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1 
                r += 1
        return res
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        for i in range(len(s)):

            l, r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1 
                r +=1 
            l, r = i,i+1 
            while l >=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1 
                r +=1 
        return count
class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)

            if i +1 < len(s) and (
                s[i]=='1' or s[i]== '2' and s[i+1] in '0123456'
            ):
                res += dfs(i+2)
            
            dp[i] = res
            return res
        return dfs(0)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ''

        resLen = 0


        for i in range(len(s)):

            l,r = i,i 

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # checking if there is a palindrom while blooming out 

                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1 
                
                l -= 1
                r += 1
            
            l, r = i, i+ 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                # checking if there is a palindrom while blooming out 

                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1 
                
                l -= 1
                r += 1
        return res
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        for i in range(len(s)):
            count += self.helper(s, i, i)
            count += self.helper(s, i, i+1)
        return count
    
    def helper(self, s, l , r):
        res = 0 

        while l >= 0 and r < len(s) and s[l] == s[r]:
            res +=1 
            l -= 1
            r+=1 
        return res


class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s): 1}

        # i will need to do DFS for this 

        def dfs(i):

            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0 
            
            res = dfs(i+1)

            if i + 1 < len(s) and (
                s[i]=='1' or s[i]=='2' and s[i+1] in '0123456'
            ):
                res += dfs(i+2)
            
            dp[i] = res 

            return res 
        return dfs(0)
class Solution:
    def numDecodings(self, s: str) -> int:
        

        dp = {len(s): 1}

        for i in range(len(s)-1, -1, -1):
            # going backwards

            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]