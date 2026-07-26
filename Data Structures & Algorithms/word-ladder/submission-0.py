class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 #there are other cases when return 0
        if beginWord == endWord:
            return 1
        ans=1
        l=len(beginWord)
        pattern={} # the list of elements sharing the same pattern (which is the key)
        visited={}
        def listpat(word):
            ans=[]
            for i in range(l):
                pat=word[:i]+'*'+word[i+1:]
                ans.append(pat)
            return ans
                
        for word in  wordList:
            pat = listpat(word)
            visited[word]=False
            for p in pat:
                pattern[p]=pattern.get(p,[])
                pattern[p].append(word)
        
        queue=deque()
        queue.append(beginWord)
        visited[beginWord]=True
        while queue:
            s=len(queue)
            ans+=1
            for i in range(s):
                pat = listpat(queue.popleft())
                for p in pat:
                    if p in pattern:
                        for nei in pattern[p]:
                            if(visited[nei]):
                                continue
                            if(nei==endWord):
                                return ans
                            queue.append(nei)
                            visited[nei]=True
        return 0
