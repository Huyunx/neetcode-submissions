class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c=False,False,False
        xt,yt,zt=target
        for x,y,z in triplets:
            if(x==xt and y<=yt and z<=zt):
                a=True
            if(x<=xt and y==yt and z<=zt):
                b=True
            if(x<=xt and y<=yt and z==zt):
                c=True
        if(a and b and c):
            return True
        return False