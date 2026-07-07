class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans: str = "0"
        sum_d: int = 0
        for i in str(n):
            if int(i):
                ans += i
                sum_d += int(i)
        return int(ans) * sum_d