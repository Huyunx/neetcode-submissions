class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=1
        currmax=nums[0]
        currmin=nums[0]
        ans=currmax
        for n in range(1,len(nums)):
            i=nums[n]
            if(i>=0):
                
                currmax=max(currmax*i,i)
                currmin=min(currmin*i,i)

            if(i<0):
                a=currmax
                currmax=max(currmin*i,i)
                currmin=min(a*i,i)
            ans=max(currmax,ans)
        return ans

