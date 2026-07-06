class PrefixTree:

    def __init__(self):
        self.val=''
        self.children={}
        self.end=False

    def insert(self, word: str) -> None:
        node=self
        for i in word:
            
            if (not node.children) or (not (i in node.children)):
                child=PrefixTree()
                child.val=i
                node.children[i]=child
            node=node.children[i]
        node.end=True
       # node.children=None that one was totally unnecessary 

    def search(self, word: str) -> bool:
        node=self
        for i in word:
            if i in node.children:
                node=node.children[i]
            else:
                return False
        if node.end:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node=self
        for i in prefix:
            if i in node.children:
                node=node.children[i]
            else:
                return False
        return True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        storedwords=PrefixTree()
        for i in words:
            storedwords.insert(i)
        ans=set()
        def searc(string,i,j):
           
            if(i>=len(board) or j>=len(board[0]) or i<0 or j<0 or board[i][j]=='#'):
                return
            a=board[i][j]
            string = string + a
            board[i][j]='#'
            have=storedwords.search(string)
            if(have):
                ans.add(string)
            if(have or storedwords.startsWith(string)):
                searc(string,i+1,j)
                searc(string,i,j+1)
                searc(string,i-1,j)
                searc(string,i,j-1)
            board[i][j]=a
            return
        for i in range(0, len(board)):
            for j in range(0,len(board[0])):
                searc('',i,j)
        return list(ans)
            