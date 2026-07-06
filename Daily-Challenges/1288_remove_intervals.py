class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        dic: dict = {}
        stack: list[int] = []
        for start, end in intervals:
            if not dic:
                dic[start] = end
                stack.append(start)
            if start not in dic:
                if dic[stack[-1]] >= end:
                    continue
                else:
                    dic[start] = end
                    stack.append(start)
            else :
                if dic[start] < end:
                    dic[start] = end
        return len(dic)