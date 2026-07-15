def gcd(a: int, b: int) ->int:
    while b:
        r = a % b       # remainder
        a, b = b, r     # Euclidean Algorithm
    return a

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n ** 2
        sumEven = n * (n + 1)

        return gcd(sumOdd, sumEven)