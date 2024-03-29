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
