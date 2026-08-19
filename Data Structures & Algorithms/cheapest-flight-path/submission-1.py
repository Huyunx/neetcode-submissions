class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        reached=set() #store pair(node,kk)reached node with kk steps if there is a new reaching path with smaller kk we can add it in the hep and dont count it as already reached
        adj={}
        for f,t,p in flights:
            adj[f]=adj.get(f,[])
            adj[f].append((p,t))
        heap=[]
        heapq.heappush(heap,(0,-1,src))#(price to src, with -1 stops, to node src)
        ans=-1
        while heap:
            price,stops, node= heapq.heappop(heap)
            if((node,stops) in reached):
                continue
            
            reached.add((node,stops))
            if(node==dst):
                ans=price
                break

            if(stops>=k):
                continue
            if(node in adj): 
                for p,des in adj[node]:
                    heapq.heappush(heap,(price+p,stops+1,des))
    

        return ans