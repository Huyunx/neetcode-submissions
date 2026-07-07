class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        ans=[]
        for i in range(len(s)):
            l=i
            r=i
            c=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                c=r-l+1
            if(c> maxlen):
                maxlen=c
                ans=[l+1,r]
            l=i
            r=i+1
            c=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                c=r-l+1
            if(c> maxlen):
                maxlen=c
                ans=[l+1,r]
        return s[ans[0]:ans[1]]
            