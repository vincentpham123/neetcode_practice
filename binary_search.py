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