#just add a 'Q at every column or row instead of trying to add at every point on grid
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        attacke=[[0 for j in range(n)]for i in range(n)]
        ans=[]
        def dfs(board,attacked,index):
            if(index == n):
                ans.append(board.copy())
                return
            i=index
            for j in range(n):
                if(attacked[i][j]):
                    continue
                else:
                    origboard=board[i]
                    board[i]=board[i][:j]+'Q'+board[i][j+1:]#slow should probably use 2d grid with chars 
                    orig = [row.copy() for row in attacked]
                    for a in range(n):
                        attacked[i][a]=1
                        attacked[a][j]=1
                        if(i+a< n and j+a<n):
                            attacked[i+a][j+a]=1
                        if(i-a>=0 and j-a>=0):
                            attacked[i-a][j-a]=1
                        if(i-a>=0 and j+a<n):
                            attacked[i-a][j+a]=1
                        if(i+a< n and j-a>=0):
                            attacked[i+a][j-a]=1
                    
                    dfs(board,attacked,index+1)

                    board[i]= origboard
                    attacked=orig

            return 
        board=[]
        s=''
        for i in range(n):
            s+='.'
        for i in range(n):
            board.append(s)
        dfs(board,attacke,0) 
        return ans