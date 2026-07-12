class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        
        ranks: dict = {num: i+1 for i, num in enumerate(sorted(set(arr)))}

        return [ranks[num] for num in arr]