class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)
        m=int((l+r)/2)
        while l!=r:
            m=int((l+r)/2)
            if(nums[m]<nums[0]):
                r=m
            else :
                l=m+1
        
        return nums[l%len(nums)]