class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s=0
        sumnums=0
        maxnotwrap=nums[0]
        for i in nums:
            sumnums+=i
            s+=i
            maxnotwrap=max(maxnotwrap,s)
            if(s<0):
                s=0
        s=0
        e=nums[0]
        for i in nums[1:len(nums)-1]:
            s+=i
            e=min(e,s)
            if(s>0):
                s=0
        return max(maxnotwrap,sumnums-e)