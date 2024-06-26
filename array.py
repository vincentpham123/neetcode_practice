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

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        # i bascially just need to check if there are repitions in the rows, cols and square

        for r in range(9):
            for c in range(9):

                if board[r][c]=='.':
                    continue
                elif (
                    board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r//3, c//3)]
                ):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r//3, c//3)].add(board[r][c])
        return True
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        result = float('inf')
        left = 0

        right = sum(grid[0])
        # this will allow us to iterate right by subtracting
        
        for a,b in zip(grid[0], grid[1]):
            # this will return pairs
            # this will allow us to either go down or right 

            right -= a
            
            result = min(result, max(right, left))

            left += b
        return result
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # the trick to threeSum like all sums is to sort

        nums.sort()

        # the way to avoid diplicate sets is to move the pointer so its not the same as the last or greater than 0
        res = []
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0. and a == nums[i-1]:
                continue 
            
            l,r = i+1, len(nums)-1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    
                    # need to skeep duplicates
                    while nums[l] == nums[l-1] and l <r:
                        l+=1
        return res
            