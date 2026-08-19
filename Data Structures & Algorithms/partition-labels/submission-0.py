#when whant to optimize by time throw a hashmap
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastseen={}
        for i,c in enumerate(s):
            lastseen[c]=i
        endd=0
        startt=0
        ans=[]
        for i,c in enumerate(s):
            if(lastseen[c]>endd):
                endd=lastseen[c]
            if(i==endd):
                ans.append(endd-startt+1)
                startt=endd+1
                continue
            
        return ans
