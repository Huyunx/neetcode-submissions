class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj={}
        for i in range(len(points)):
            for j in range(len(points)):
                if(i==j):
                    continue
                n1=points[i]
                n2=points[j]
                wei=abs(n1[0]-n2[0])+abs(n1[1]-n2[1])
                adj[i]=adj.get(i, [])


                adj[i].append((wei,j))
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
            if(node in adj):
                for weitonei,nei in adj[node]:
                    if(nei not in reached):
                        heapq.heappush(heap,(weitonei,nei))
            if(len(reached)==len(points)):
                break
                    
        return cost

