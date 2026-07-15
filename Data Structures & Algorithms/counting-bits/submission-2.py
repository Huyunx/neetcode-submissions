class Solution:
    def countBits(self, n: int) -> List[int]:
        offset=1
        a=0
        res=[0]
        for i in range(1,n+1):
            res.append(res[i-offset]+1)
            a+=1
            if(a==offset):
                a=0
                offset*=2
        return res


