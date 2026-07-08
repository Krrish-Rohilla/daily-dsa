class Solution:
    def isValid(self, s: str) -> bool:
        stack: list = []
        for i in s:
            if i in {")", "}", "]"} and stack:
                if i == ")" and stack.pop() == "(":
                    continue
                elif i == "}" and stack.pop() == "{":
                    continue
                elif i == "]" and stack.pop() == "[":
                    continue
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True