from functools import lru_cache
@lru_cache(maxsize=3000)
def check(n: int, x: int) -> bool:
    l = n % 10
    while n >= 10:
        n = n//10
    return n == x and l == x

class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if check(s,x): c += 1
        return c