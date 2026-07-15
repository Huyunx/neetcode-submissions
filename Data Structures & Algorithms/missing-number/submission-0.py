# sum everything 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for i in range(len(nums)):
            res ^= (i^nums[i])
        res ^=n
        return res