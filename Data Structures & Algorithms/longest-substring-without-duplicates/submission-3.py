class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        start=0
        maxxlen=0
        for end,n in enumerate(s):
            while n in window:
                window.remove(s[start])
                start+=1
            window.add(n)
            l=len(window)
            if(maxxlen<l):
                maxxlen=l
        return maxxlen


