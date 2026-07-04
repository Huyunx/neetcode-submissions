class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        def ex(r,c,i):#the frontier index of word
            if(i==len(word)):
                return True
            if(r==len(board) or c==len(board[0]) or r==-1 or c==-1):
                return False
            if(visited[r][c]):
                return False
            if(board[r][c]==word[i]):
                visited[r][c] = True
                found = (
                    ex(r+1, c, i+1) or
                    ex(r-1, c, i+1) or
                    ex(r, c+1, i+1) or
                    ex(r, c-1, i+1)
                )

                visited[r][c] = False
                #wtf why need backtrade
                return found
            else:
                return False
        ans=False
        for i in  range(len(board)):
            for j in range(len(board[0])):
                #visited = [[False] * len(board[0]) for _ in range(len(board))]
                ans=ans or ex(i,j,0)

        return ans