class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        frontier=intervals[0]
        def overlap(int1,int2):
            if(int1[1]<=int2[0]):
                return False
            else:
                return True
        ans=0
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if(overlap(frontier,interval)):
                if(frontier[1]>interval[1]):
                    frontier=interval
                ans+=1
            else:
                frontier=interval

        return ans