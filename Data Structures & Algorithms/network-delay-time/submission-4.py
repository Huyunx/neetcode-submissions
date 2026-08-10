#leme do it in python as well
#taking the shortest path from the heap always give you the next globally shortest path if it happen to lead to a node n for first time then this is the shortest path to n.   and adding the paths only from the node of the curr min path is enough to ensure that the next min path is inside the heap as any other further paths are definitely longer than the one that we have in the heap 
import heapq
class Solution:
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap=[]
        adj={}
        for u,v,w in times:
            adj[u]=adj.get(u,[])
            adj[u].append([v,w])

        heapq.heappush(heap,(0,k))
        visitednodes=set()
        maxi=0
        while heap:
            
            (shortestpath,tonode) = heapq.heappop(heap)
            if(tonode in visitednodes):
                continue
            visitednodes.add(tonode)
            maxi=max(maxi,shortestpath)
            if tonode in adj:
                for nextnode,weight in adj[tonode]:
                    heapq.heappush(heap,(shortestpath+weight,nextnode))
        if len(visitednodes)!= n:
            return -1
        return maxi

