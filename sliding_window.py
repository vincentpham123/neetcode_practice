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
def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        # this is used to keep track of the two char counts in s 

        maxf = float('-inf')

        left = 0 

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            # i will either add the current count of the string or add 0 if it doesnt exist yet 

            maxf = max(maxf, count[s[r]])

            if (r - left + 1) - maxf > k:
                # the max amount of letters is replaced 
                count[s[left]] -= 1 
                left += 1 
        return (r-left+1 )
  def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT , window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)

        res, resLen= [-1,-1], float("inf")

        left = 0 

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c,0)
            #checking if the window is the same as countT

            if c in countT and window[c] == countT[c]:
                have +=1 
                # if a character is in the substring, have increases by 1
            while have == need:
                # update our result
                # once we know our window has all letters, we can update, and move our window   
                if (right-left+1) < resLen:
                    # so if the current substring with all the letters in t 
                    # are less than resLen, then we update
                    res = [left,right]
                    resLen = right - left + 1
                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -=1 
                    # if the current letter at the left is in t, and we have subtracted eith the line before, we reduce the have by 1, we have taken out a letter from t in the sliding window 
                left += 1
        
        l, r = res 

        return s[l: r +1] if resLen != float('inf') else ""

                # we are now udpating the window
                    
                    


        # cant return based on left and right because right will go to the end 



