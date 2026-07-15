class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1

        while n:
            digit = n % 10
            s += digit
            p *= digit
            n //= 10
        
        return p - s