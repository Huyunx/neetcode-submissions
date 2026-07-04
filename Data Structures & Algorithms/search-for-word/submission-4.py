class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def ex(r,c,i):#the frontier index of word
            if(i==len(word)):
                return True
            if(r==len(board) or c==len(board[0]) or r==-1 or c==-1):
                return False
            if(board[r][c]==word[i]):
                a=board[r][c]
                board[r][c]='#'
                found = (
                    ex(r+1, c, i+1) or
                    ex(r-1, c, i+1) or
                    ex(r, c+1, i+1) or
                    ex(r, c-1, i+1)
                )
                board[r][c]=a
                
                #wtf why need backtrade
                return found
            else:
                return False
        ans=False
        for i in  range(len(board)):
            for j in range(len(board[0])):
                ans=ans or ex(i,j,0)

        return ans