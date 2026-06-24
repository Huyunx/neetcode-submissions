class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        tset=set(t)
        freq={}
        freqt={}
        leng=len(s)
        ansr=-1
        ansl=0
        for i in t:
            freqt[i]=freqt.get(i,0)+1
        checklist= set(t)
        for r in range(len(s)):
            if(l==len(s)):
                break
            while s[l] not in tset:
                l+=1
                if(l==len(s)):
                    break
            if(s[r] in tset):
                freq[s[r]]=freq.get(s[r],0)+1
                if freq[s[r]] == freqt[s[r]]:
                    checklist.remove(s[r])
                while not checklist:
                    if leng >= r-l+1:
                        leng=r-l+1
                        ansr=r
                        ansl=l
                        
                    freq[s[l]] -= 1
                    if freq[s[l]] < freqt[s[l]]:
                        checklist.add(s[l])
                    
                    l+=1
                    if(l==len(s)):
                        break
                    while s[l] not in tset:
                        l+=1
                        if(l==len(s)):
                            break
                    
        res=""
        for i in range(ansl,ansr+1):
            res += s[i]
        return res
                

