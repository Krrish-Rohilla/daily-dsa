@cache
def backer(n: int, l: int, r: int, curr = 1, prev = None, up = None):
    if curr > n:
        return 1
    sub_sum = 0
    for x in range(l, r+1):
        if curr == 1: 
            sub_sum += backer(n, l, r, 2, x, None)
        elif curr == 2:
            if prev > x: 
                sub_sum += backer(n, l, r, 3, x, False)
            elif prev < x:
                sub_sum += backer(n, l, r, 3, x, True)
        else:
            if up and x < prev: 
                sub_sum += backer(n, l, r, curr+1, x, False)
            elif not up and x > prev: 
                sub_sum += backer(n, l, r, curr+1, x, True)
    return sub_sum

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int: 
        backer.cache_clear()
        return backer(n, l, r, 1, None, None) % (10**9 + 7)