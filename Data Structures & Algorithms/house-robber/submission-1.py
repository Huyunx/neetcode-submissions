class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n1=nums[1]
        n2=nums[0]
        m=max(n1,n2)
        for i in range(2,len(nums)):
            a=n1
            n1=max(n2+nums[i],n1-nums[i-1]+nums[i])
            m=max(m,n1)
            n2=a
        return m