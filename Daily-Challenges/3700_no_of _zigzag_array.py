@cache
def backer(curr: int, v: int, up: bool, n: int, k: int) -> int:
    if curr > n: return 1
    
    if up:
        if v == k - 1: return 0
        return backer(curr + 1, v + 1, False, n, k) + backer(curr, v + 1, True, n, k)
        
    else:
        if v == 0: return 0
        return backer(curr + 1, v - 1, True, n, k) + backer(curr, v - 1, False, n, k)

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r - l + 1     
        backer.cache_clear()

        total = 0
        for first_val in range(k):
            total += backer(2, first_val, True, n, k)
            total += backer(2, first_val, False, n, k)

        return total % (10**9 + 7)