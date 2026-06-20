class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ans,p = [],0
        for i in range(1,n+1):
            check = target[p] if p<len(target) else -1
            if check == -1: continue
            if check == i:
                ans.append("Push")
                p += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans