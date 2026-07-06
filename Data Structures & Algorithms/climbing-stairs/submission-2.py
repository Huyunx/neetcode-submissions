class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==0 or n==1):
            return 1
        i1=1
        i2=1
        ans=i1+i2
        for i in range(0,n-1):
            ans=i1+i2
            a=i1
            i1=ans
            i2=a
        return ans