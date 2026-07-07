class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return max(nums[0],nums[1])
        n1=max(nums[1],nums[0])
        n2=nums[0]
        m1=n1
        for i in range(2,len(nums)-1):
            a=n1
            n1=max(n1,n2+nums[i])
            m1=max(n1,m1)
            n2=a
        n1 = max(nums[1],nums[2])
        n2 = nums[1]
        m2=n1
        for i in range(3,len(nums)):
            a=n1
            n1=max(n1,n2+nums[i])
            m2=max(n1,m1)
            n2=a
        return max(m1,m2)