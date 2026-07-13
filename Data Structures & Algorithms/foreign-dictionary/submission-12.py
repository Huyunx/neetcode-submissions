class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={}
        roots=set()
        nodes=set()
        for i in words:
            for j in i:
                roots.add(j)
                nodes.add(j)
        if(len(words)==1):
            return words[0]
        for i in range(len(words)-1):
            j=i+1
            a=0
            while a!=min(len(words[i]),len(words[j])) and words[i][a]==words[j][a]:
                a+=1
            if(a==len(words[j]) and len(words[j])<len(words[i])):        
                return ""
            if(a==len(words[i])):
                continue
            else:
                adj[words[i][a]]=adj.get(words[i][a],[])
                adj[words[i][a]].append(words[j][a])
                roots.discard(words[j][a])
        visited={}
        visiting =set()
        foundcycle=False
        
        def longest_path_dfsing_from(node):
            nonlocal foundcycle
            if(node in visiting):
                foundcycle=True
            visiting.add(node)
            if(node in visited):
                visiting.discard(node)
                return ''
            visited[node]=True
            
            if node not in adj:
                visiting.discard(node)
                return node
            
            
            ret=''
            for i in adj[node]:
                ret=ret+longest_path_dfsing_from(i) 
            visiting.discard(node)
            return ret+node
        ans=''
        for i in nodes:
            ans=ans+longest_path_dfsing_from(i)
        if(foundcycle):
            return ''
        return ans[::-1]
            #now do topological sort/ inorder traversal from these roots
            


            

            
            

        