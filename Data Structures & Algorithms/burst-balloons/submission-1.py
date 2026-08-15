class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        dp ={}
        
        def maxcol(i,j):
            ret=0
            if((i,j) in dp ):
                return dp[(i,j)]
            l=1
            r=1
            if(j+1<len(nums)):
                r=nums[j+1]
            if(i-1>=0):
                l=nums[i-1]
            if(i==j):
                return l*r*nums[i]
            if(i>j):
                return 0
            for k in range(i,j+1):
                ret=max(ret,nums[k]*l*r+maxcol(i,k-1)+maxcol(k+1,j))
            dp[(i,j)]=ret
            return ret
        return maxcol(0,len(nums)-1)
      

