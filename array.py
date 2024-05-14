class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # [1,2,3,4]
        # [1,1,2,6] # each index is the product of every element to the left of it 
        #[24,24,12,4] # each index is the product of every element to the right of it, starting from right

        # the pattern is that if we multiply the ith place of both of these arrays, we obtain the answer

        res = [1 for i in range(len(nums))]


        # now i will create the first array

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        

        productfromright = 1 

        for i in range(len(nums)-1,-1,-1):
            #going backwards
            res[i] *= productfromright

            #need to update the productfromright by mulitplying similar to the first for loop
            productfromright *= nums[i]
        return res
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(2):
            for n in nums:
                res.append(n)
        return res
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        rightMax = -1

        for i in range(len(arr)-1,-1,-1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # the best thing to do is to have another array
        # that is keeping track of the product to the right

        # so we can keep an array that stores the product to the left of i in i 

        res = [1] * len(nums)

        for i in range(1,len(res)):
            res[i] = res[i-1]* nums[i-1]

            # looking at this, we are basically storing the product to the left 
            # at i, so at res[1] = res[0] (1) * nums[1]
            # we continue this 
            # we dont update the first index, because there is nothing to the left 
        postFix = 1

        # now we have to fix it
        # the idea is to go from the right
        # now that we have every product from the left
        # we muliply it with the product from the right

        for i in range(len(res)-1,-1,-1):
            res[i] *= postFix
            postFix *= nums[i]
            # we have to update postFix to reflect the product from the right

            # next loop, itll be 4, then 12, then 24
        return res

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0:0}

        for r in wall:
            total = 0 
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)
        return len(wall) - max(countGap.values())
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # i will need three 3 pointers
        # 1 for the 0s, 1s and 2s 

        low = 0 
        mid = 0 
        high = len(nums)-1

        while mid <= high:
            
            # we are going to sort from the middle

            if nums[mid]==0:
                #if its a zero, we know we exchange with our pointer for zero(low)
                nums[mid], nums[low] = nums[low], nums[mid]

                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1 
            else:
                # if nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # we dont need to worry about what number we're exchanging with high 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # the trick to this problem is to check for +1 for a number in nums

        # i need a constant look up time to check for +1 in nums

        numSet = set(nums)


        result = 0 

        for n in nums:
            
            streak = 1
            while (n+streak) in numSet:
                streak +=1
            result = max(streak, result)
        return result
