class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        lowest_price = float("inf")
        for i in prices:

            lowest_price = min(i, lowest_price)

            curr_profit = i - lowest_price 

            max_profit = max(curr_profit, max_profit)
        return max_profit

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0

        charSet = set()
        substring = 0
        for i in range(len(s)):
            
            # i will use the set to catch duplicates 
            # what happens when a s[i] is already in the set, 
            # that means, that the substring is no long good, 
            # i have to keep removing from the substring, until the s[i] is no longer in it

            while s[i] in charSet:
                charSet.remove(s[left])
                left+=1 
            
            #each iteration, i will add a letter to th set 

            charSet.add(s[i])

            #then i udpate the max substring length 
            substring = max(substring, i - left +1 )
            # i am adding the 1 to account for i starting at 0 
        return substring
