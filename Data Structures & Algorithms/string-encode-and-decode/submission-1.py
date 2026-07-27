class Solution:
#[neet,code,4#got]
#[4#neet,4#code,4#4#got] instead of 44got and we dont know to take 4 or 44
    def encode(self, strs: List[str]) -> str:
        ans=''
        for s in strs:
            ans=ans+str(len(s))+'#'+s

        return ans
    def decode(self, s: str) -> List[str]:
        last=0
        ans=[]
        i=0
        while i<len(s):
            if(s[i]=='#'):
                l=int(s[last:i])
                ans.append(s[i+1:i+l+1])
                last=i+l+1
                i+=l
            i+=1
        return ans