class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        
        for i in range(len(points)):
            x,y=points[i]
            heapq.heappush(heap,(x**2+y**2,i))
        ans=[]
        for i in range(k):
            a=heapq.heappop(heap)
            ans.append(points[a[1]])
        return ans