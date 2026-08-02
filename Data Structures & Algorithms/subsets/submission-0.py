class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        def rec(n):
            if n==len(nums)-1:
                return [[],[nums[n]]]
            a=rec(n+1)
            include=[]
            for i in a:
                include.append([nums[n]]+i)
            exclude=rec(n+1)

            return include + exclude
        return rec(0)