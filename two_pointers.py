class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i will have a pointer at the end and in the beginningt 
        # if a pointer is pointing at a space or non alphabet, i will keep increasing or decreasing until it is
        left = 0 
        right = len(s)-1
        
        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left+=1
            # checking for left is less than right in the case that a string is all non-alphabet
            
            while right > left and not self.alphaNum(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right -1
        return True
        # new =''
        # for a in s:
        #     if a.isalpha() or a.isdigit():
        #         new+= a.lower()

        # return (new == new[::-1])
    
    ## alterntative soluytion that doesnt use two pointers


    def alphaNum(self, c):
        return (c.isalpha() or c.isdigit())
    
     
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # only6 one extra space
    # i can create a hash to store 
    
        hash = {}
        for idx, x in enumerate(numbers):
            
            other_num = target - x 
            
            if other_num in hash:
                return [hash[other_num]+1, idx+1]

            hash[x] = idx
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) -1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum < target:
                left+=1 
            elif curSum > target:
                right-=1 
            else:
                return [left+1, right +1]
        def threeSum(self, nums: List[int]) -> List[List[int]]:
        
            res = []
            nums.sort()

            for i, a in enumerate(nums):
                if a > 0:
                    break 
                
                if i >0 and a == nums[i-1]:
                    continue 
                

                l, r = i +1, len(nums)-1 

                while l < r:
                    threesum = a + nums[l] + nums[r]

                    if threesum < 0:
                        l +=1 
                    elif threesum > 0:
                        r -=1 
                    else:
                        res.append( [a, nums[l], nums[r]])
                        l+=1 
                        r-=1
                        # need to check for dupes 

                        while l < r and nums[l] == nums[l-1]:
                            l+=1 
            return res