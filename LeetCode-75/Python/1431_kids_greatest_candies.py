class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= m:
                result.append(True)
            else :
                result.append(False)
        return result