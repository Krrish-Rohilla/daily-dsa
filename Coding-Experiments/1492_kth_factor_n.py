class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        c , i = 0 , 1
        while True:
            if c == k: break
            if i > n: return -1
            if n % i == 0: c += 1
            i += 1
        return i-1