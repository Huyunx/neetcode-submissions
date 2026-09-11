class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        ans=0
        while l<r:
            maxl=max(maxl,height[l])
            maxr=max(maxr,height[r])
            #print(l,r,file.sys.stderr)
            if(height[l]>=height[r]):
                ans+=(maxr-height[r])
                r-=1
            else:
                ans+=(maxl-height[l])
                l+=1
        return ans