class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_no = 0
        c = 0
        for i in nums:
            p = True if i else False
            if p: c += 1
            else:
                max_no = max(max_no,c)
                c = 0
        return max(max_no,c)