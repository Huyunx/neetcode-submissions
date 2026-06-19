class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterhavingtimes = [0]*26
        anagram = {
        }
        for str in strs:
            letterhavingtimes = [0]*26
            for i in str:
                
                alphanetorder = ord(i)-ord('a')
                letterhavingtimes[alphanetorder] += 1
            key= tuple(letterhavingtimes)
            if key in anagram:
                anagram[key].append(str)
            else:
                anagram[key] = [str]
        ans = []
        for i in anagram:
            ans.append(anagram[i])
        return ans
