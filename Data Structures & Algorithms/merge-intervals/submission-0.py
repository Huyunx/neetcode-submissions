class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(int1,int2):
            if(int1[1]<int2[0]):
                return False
            return True
        intervals.sort()
        frontier=intervals[0]
        res=[]
        added=False
        for i in range(1,len(intervals)):
            interval=intervals[i]
            if(overlap(frontier,interval)):
                frontier[1]=max(frontier[1],interval[1])
                added=False

            else:
                added=True
                res.append(frontier)   
                frontier=interval
       
        res.append(frontier)
        return res

    
