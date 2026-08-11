class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        mapp={
         '2':['a','b','c'],
         '3':['d','e','f'],
         '4':['g','h','i'],
         '5':['j','k','l'],
         '6':['m','n','o'],
         '7':['p','q','r','s'],
         '8':['t','u','v'],
         '9':['w','x','y','z']
        }
        if(digits==""):
            return ans
        def dfs(s,fronti):
            if(fronti==len(digits)):
                ans.append(s)
                return

            currdigit=digits[fronti]
            for letter in mapp[currdigit]:
                dfs(s+letter,fronti+1)
            return 
        dfs('',0)
        return ans