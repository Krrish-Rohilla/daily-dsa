class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        ans: list[str] = [x for x in patterns if x in word]
        return len(ans)