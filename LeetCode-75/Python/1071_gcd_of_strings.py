class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 +str2 != str2 + str1 :
            return ""

        s1 = str1
        s2 = str2
        l1 = len(s1)
        l2 = len(s2)
        t1 = s1
        t2 = s2

        if l1>l2 :
            s = s2
        else:
            s = s1
        t = s
        l = len(s)

        for i in range(l-1,-1,-1):
            t = s[:i+1]
            if t * (l1 // len(t)) == s1 and l1 % len(t) == 0 and t*(l2//len(t)) == s2 and l2 % len(t) == 0:
                break
        return t