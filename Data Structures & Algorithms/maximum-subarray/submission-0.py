class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev=nums[0]
        if(len(nums)==1):
            return nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if(prev<=0):
                prev=nums[i]
            else:
                prev=nums[i]+prev
            ans=max(ans,prev)
        return ans
        