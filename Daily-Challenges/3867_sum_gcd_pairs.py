def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        maxN = 0
        prefixGcd: list[int] = []

        for n in nums:
            maxN = max(maxN, n)
            prefixGcd.append(gcd(n, maxN))
        
        l = len(nums)
        s = 0
        prefixGcd.sort()

        for i in range(l//2):
            s += gcd(prefixGcd[i], prefixGcd[l-i-1])
        
        return s