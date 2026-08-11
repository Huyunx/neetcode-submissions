#just add a 'Q at every column or row instead of trying to add at every point on grid
#visited[0]=rows
#visited[1]=main diag lef up to rightbottom [j-i]
#visited[2]=second diag   [n-1-j-i] 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        attacke=[set(),set(),set()]
        ans=[]
        def dfs(board,visited,index):
            if(index == n):
                ans.append(board.copy())
                return
            i=index
            for j in range(n):
                if(j in visited[0] or j-i in visited[1] or n-1-j-i in visited[2]):
                    continue
                else:
                    origboard=board[i]
                    board[i]=board[i][:j]+'Q'+board[i][j+1:]#slow should probably use 2d grid with chars 
                    
                    
                    visited[0].add(j)
                    visited[1].add(j-i)
                    visited[2].add(n-1-j-i)

                    dfs(board,visited,index+1)
                    
                    visited[0].discard(j)
                    visited[1].discard(j-i)
                    visited[2].discard(n-1-j-i)
                    board[i]= origboard

                   

            return 
        board=[]
        s=''
        for i in range(n):
            s+='.'
        for i in range(n):
            board.append(s)
        dfs(board,attacke,0) 
        return ans