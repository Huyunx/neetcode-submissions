"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s=[]
        e=[]

        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        s.sort()
        e.sort()
        spoint=0
        epoint=0
        res=0
        ans=0
        for i in s:
            res+=1
            while(e[epoint]<=i):
                res-=1
                epoint+=1
            ans=max(ans,res)
        return ans
        