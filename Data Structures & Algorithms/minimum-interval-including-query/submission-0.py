class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        orig=queries.copy()
        intervals.sort()
        queries.sort()
        heap=[]
        j=0
        ans={}
        for i in queries:
            while heap and heap[0][1]<i:
                heapq.heappop(heap)
            while j!=len(intervals) and intervals[j][0]<=i:
                start=intervals[j][0]
                end=intervals[j][1]
                if start<=i and i<=end:
                    heapq.heappush(heap,(end-start+1,end))
                j+=1
            ans[i]=-1
            if(heap):
                ans[i] = heap[0][0]
        res=[]
        for i in orig:
            res.append(ans[i])
        return res