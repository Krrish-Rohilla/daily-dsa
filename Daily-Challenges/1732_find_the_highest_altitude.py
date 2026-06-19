class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt,s = [0],0
        for i in gain:
            s += i
            alt.append(s)
        return max(alt)