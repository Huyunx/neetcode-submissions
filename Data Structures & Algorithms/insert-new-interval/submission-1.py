class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #ohhh too lazy to do this one, ajde ajde
        res=[]
        aped=False
        for interval in intervals:

            if interval[0]>newInterval[1]:
                if not aped:
                    res.append(newInterval)
                aped=True
                res.append(interval)
            elif interval[1]<newInterval[0]:
                res.append(interval)
                pass
            else:
                #overlap
                merged=[min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
                newInterval=merged
                aped=False
        if(not aped):
            res.append(newInterval)
        return res
