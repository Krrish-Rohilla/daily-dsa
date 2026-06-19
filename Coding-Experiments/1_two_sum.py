class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ss= set()
        for j,i in enumerate(nums):
            if target-i in ss:
                return [nums.index(target-i),j]
            ss.add(i)
        return []