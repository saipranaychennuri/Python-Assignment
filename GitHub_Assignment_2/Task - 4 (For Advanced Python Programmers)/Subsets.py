class Solution:
    def subsets(self, nums):
        res = []
        
        def backtrack(start, subset):
            res.append(subset)
            for i in range(start, len(nums)):
                backtrack(i+1, subset+[nums[i]])
                
        backtrack(0, [])
        return res
s=Solution()
print(s.subsets([0]))