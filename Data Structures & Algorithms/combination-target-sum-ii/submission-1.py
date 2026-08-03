class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sumstartwithnum={

        }#keep if target sum that is formed by trying to find a combination of
        #certain starting value is already being processed
        candidates.sort()
        ans=[] 
        def dfs(target,firstindex,currcombination):
            if(firstindex==len(candidates)):
                return 
            a=candidates[firstindex]
        
            if(target<0):
                return
            if target==a:
                ans.append(currcombination+[a])
                return
                
           
            dfs(target-candidates[firstindex],firstindex+1,currcombination+[a])
            i=1
            while (firstindex+i<len(candidates) and candidates[firstindex+i]==candidates[firstindex+i-1]):
                i+=1
            dfs(target,firstindex+i,currcombination)
            return 
          
        dfs(target,0,[])
        return ans