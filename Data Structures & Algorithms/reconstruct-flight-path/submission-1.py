#Eulerian path

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj={}
        numbertickets={}
        for i in tickets:
            from1=i[0]
            to1=i[1]
            numbertickets[(from1,to1)]=numbertickets.get((from1,to1),0)
            numbertickets[(from1,to1)]+=1
            adj[from1]=adj.get(from1,[])
            adj[from1].append(to1)
        for i in adj:
            adj[i].sort()        
        def cantraverseallfrom(node,edgesituation,visitednum):
            if(visitednum==len(tickets)):
                return [1,[node]]
            if(node in adj):
                for nextnode in adj[node]:
                    if(edgesituation[(node,nextnode)]!=0):
                        edgesituation[(node,nextnode)]-=1
                        res=cantraverseallfrom(nextnode,edgesituation,visitednum+1)
                        if(res[0]):
                            res[1].append(node) 
                            return res
                        edgesituation[(node,nextnode)]+=1
            return [0,[]]
        ans=cantraverseallfrom("JFK",numbertickets,0)[1][::-1]
        return ans