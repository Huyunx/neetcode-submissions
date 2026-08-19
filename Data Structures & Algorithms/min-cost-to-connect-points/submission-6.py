class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap=[]
        reached=set()
        heapq.heappush(heap,(0,0))
        cost=0
        while heap:
            wei,node=heapq.heappop(heap)
            if(node in reached):
                continue
            cost+=wei
            reached.add(node)
            
            for nei,(x,y) in enumerate(points):
                x1=points[node][0]
                y1=points[node][1]
                weitonei=abs(x1-x)+abs(y-y1)
                if(nei not in reached):
                    heapq.heappush(heap,(weitonei,nei))
            if(len(reached)==len(points)):
                break
                    
        return cost

