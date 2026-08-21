class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if(len(piles)>h):
            pass
        maxp=0
        for i in piles:
            maxp=max(i,maxp)
        l=1
        r=maxp
        mink=maxp
        while True:
            m=(l+r)//2
            neededh=0
            if(l>r):
                break
            for i in piles:
                neededh+=math.ceil(i / m)
            if(neededh>h):
                l=m+1
            if(neededh<=h):
                mink=min(mink,m)
                r=m-1
        return mink