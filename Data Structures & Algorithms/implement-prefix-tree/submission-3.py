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
        
        