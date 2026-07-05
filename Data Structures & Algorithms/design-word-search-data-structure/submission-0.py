class WordDictionary:

    def __init__(self):
        self.val=''
        self.children={}
        self.end=False
    def addWord(self, word: str) -> None:
        node=self
        for i in word:
            if(i not in node.children):
                child=WordDictionary()
                child.val=i
                node.children[i]=child
            node=node.children[i]
        node.end=True

    def search(self, word: str) -> bool:
        def isit(node,frontindex):
            l=len(word)
            for i in range(frontindex,l):
                n=word[i]
                if(n=='.'):
                    found=False
                    for j in node.children:
                        found=found or isit(node.children[j],i+1)
                    return found
                if(n in node.children):
                    node=node.children[n]
                else:
                    return False
            if(node.end):
                return True
            else:
                return False
            
        return isit(self,0)