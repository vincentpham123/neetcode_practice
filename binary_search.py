class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
            left = 0 
            right = len(nums)-1

            while left <= right:
                mid = left + ((right-left)//2)
                # the above will provide the midpoint to check

                if nums[mid]<target:
                    left = mid+1
                elif nums[mid]>target:
                    right = mid-1 
                else:
                    return mid 
            return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            colCount = len(matrix[0])
            rowCount = len(matrix)
            left = 0 
            right = colCount * rowCount - 1 
            # this will provide the right of the 2d matrix

            # now i just need a way to find the midpoint and compare 
            while left <= right:
                midPoint = left + ((right-left)//2)

                #this is the midpoint of an array
                #example [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
                # 0 + (12-0/2) = 6
                # with the midpoint, I now need to dive into the 2d matrix
                # what is the connection??
                # the midpoint is matrix[1][2]
                midRow = midPoint // colCount 
                # 6 / 4 which is 1
                midCol = midPoint % colCount
                # 6 % 4 which is 1 

                if matrix[midRow][midCol] < target:
                    # i know that it is on the right side
                    left = midPoint+1 
                elif matrix[midRow][midCol] > target:
                    right = midPoint - 1 
                else:
                    return True 
            return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Input: piles = [3,6,7,11], h = 8
        # 3 bananas, 6 bananas, 7 bananas, 11 bananas
        # guard will come back in 8 hours
        #Output: 4
        # koko eats 4 bananas per hour which will allow her to finish all 27 bananas in 8 hours 

        left = 1
        right = 0

        for pile in piles:
            if pile > right:
                right = pile 
        
        #now i have my left and right pointers for binary search
        result = right 

        while left <= right:
            midpoint = (right+left)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/midpoint)
                # adding up the amount of time it would take to eat banasas at midpoint pace 
            # i then compare totalTime to hours 
            if totalTime <= h:
                result = midpoint
                right = midpoint - 1 
            else:
                left = midpoint+1 
            # we onyl care if totalTime is less than H 

        return result

    def findMin(self, nums: List[int]) -> int:
    
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = start + (end - start ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])