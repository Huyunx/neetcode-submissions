class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        appearingtime = {

        }
        for i in s:
            if i not in appearingtime:
                appearingtime[i] = 1
            else:
                appearingtime[i] += 1
        for i in t:
            if (i not in appearingtime) or appearingtime[i] == 0:
                return False
            else:
                appearingtime[i] -= 1
        for i in appearingtime:
            if appearingtime[i]!=0:
                return False
        return True
