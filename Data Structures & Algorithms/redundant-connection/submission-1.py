class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #find if the edge is in a cycle if yes we can remove that
        #check for cycle  ,undirected-visited is enough, directed-visited+visiting,dfs
        
        n=len(edges)
        par = [i for i in range(n+1)] #the parent of ith node
        rank = [1]*(n+1)
        def findpar(n):
            if(par[n]==n):
                return n
            par[n] = findpar(par[n])
            return par[n]
            
        def union(n1,n2):
            a=findpar(n1)
            b=findpar(n2)
            if(a==b):
                return False
            #let's make sure before using the union function that n1 is within larger component 
            #n2 is the smaller
            if(rank[n1]>rank[n2]):
                par[b]=a
                rank[a]+=rank[par[b]]
            else:
                par[a]=b
                rank[b]+=rank[par[a]]
            return True 
        for n1,n2 in edges:
            if(not union(n1,n2)):
                return [n1,n2]

