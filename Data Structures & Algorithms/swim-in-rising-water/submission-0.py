class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[]
        n=len(grid)
        target= 0
        ans=0
        if(grid[n-1][n-1]>grid[0][0]):
            heapq.heappush(heap,(grid[n-1][n-1],(n-1,n-1)))
            ans=grid[n-1][n-1]
        else:
            heapq.heappush(heap,(grid[0][0],(0,0)))
            target=n-1
            ans=grid[0][0]
        visited = set()
        while heap:#can break when reach  0 0 or n-1 
            a=heapq.heappop(heap)
            
            postuple=a[1]
            if(postuple in visited):
                continue
            ans=max(ans,a[0])
            
            visited.add(postuple)
            i=postuple[0]
            j=postuple[1]
            if(postuple==(target-1,target) or postuple==(target+1,target) or postuple==(target,target+1) or postuple==(target,target-1)):
                break
            if(i+1<n):
                heapq.heappush(heap,(grid[i+1][j],(i+1,j)))
            if(i-1>=0):
                heapq.heappush(heap,(grid[i-1][j],(i-1,j)))
            if(j+1<n):
                heapq.heappush(heap,(grid[i][j+1],(i,j+1)))
            if(j-1>=0):
                heapq.heappush(heap,(grid[i][j-1],(i,j-1)))

        return ans
