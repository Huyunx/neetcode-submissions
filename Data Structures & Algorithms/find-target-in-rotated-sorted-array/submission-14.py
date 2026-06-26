class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        l=0
        r=len(nums)
        m=int((l+r)/2)
        while l!=r:
            m=int((l+r)/2)
            if(nums[m]<nums[0]):
                r=m
            else :
                l=m+1
        
        leng=len(nums)
        l=l%leng
        n=l
        res=-1
        r=(l-1)%leng

        while r!=l:
            
            m = (int(((r-n) % leng+(l-n) % leng)/2)+n) % leng
            if(nums[m]>target):
                r=m
            if(target>nums[m]):
                l=(m+1)%leng
            if(target==nums[m]):
                return m
            
            
        if(nums[r]==target):  
            return r
        return -1

        
        