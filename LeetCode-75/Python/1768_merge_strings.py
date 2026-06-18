class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        t = 0
        s = ""
        if l1>l2 :
            y = l1
        else :
            y = l2
        while t<y:
            if t<l1 :
                s = s + word1[t]
            if t<l2 :
                s = s + word2[t]
            t = t + 1
        return s