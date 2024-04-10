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