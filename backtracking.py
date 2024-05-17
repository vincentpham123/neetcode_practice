
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        # when i return , i want to plug in the first num 

        first = nums[0]
        rest = nums[1:]

        without_first = self.subsets(rest)
        result=[]
        for subsets in without_first:
            result.append([first , *subsets])
        return result + without_first
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
            
            cur.append(candidates[i])

            dfs(i, cur, total + candidates[i])

            cur.pop()

            dfs(i+1, cur, total)
        
        dfs(0, [],0)
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset=[]

        def backtrack(i):
            
            if i >=len(nums):
                res.append(subset.copy())
                return 

            # now we are creating the subset where we include the nums[i]
            subset.append(nums[i])
            print('include', i)
            # then we recursively call
            backtrack(i+1)

            # now we do the other tree 
            subset.pop()
            print('not include', i)
            # this is remove the most recent and bring subset back to an empty list
            backtrack(i+1)

        backtrack(0)
        return res
def permute(self, nums: List[int]) -> List[List[int]]:

    res= []

    
    # the idea is that for each number, we remove until we have a single, then add 
    if len(nums)==1:
            # we have reached the base case from all the recursive calls 
        return [nums[:]]
    for i in range(len(nums)):
        # this should let us 
        
            # in python this returns a copt 
        n = nums.pop(0)

        perms = self.permute(nums)
        # remember that nums is now [2,3]

        for i in perms:
            i.append(n)
            # now we add back the number we have popped
        res.extend(perms)
        nums.append(n)
    return res
        
        # [1,2,3]
        # for the first loop, we pop at 1 
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i,subset):

            if i == len(nums):
                res.append(subset[::])
                return 
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, subset)
        backtrack(0,[])
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def backtrack(index, sub, target):

            
            if target==0:
                result.append(sub.copy())
                return
            if target <= 0:
                return
            
            prev = -1
            # to keep track of prev to avoid duplicates

            for i in range(index, len(candidates)):
                # we start from the index to avoid adding the previous
                if prev == candidates[i]:
                    continue
                
                sub.append(candidates[i])
                backtrack(i+1, sub, target-candidates[i])
                sub.pop()
                prev = candidates[i]
            
        backtrack(0, [], target)
        return result
