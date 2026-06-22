class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+*-/":
                stack.append(int(i))
                continue

            operation = i
            b = stack.pop()
            a = stack.pop()

            if operation == "+": stack.append(a+b)
            elif operation == "-": stack.append(a-b)
            elif operation == "*": stack.append(a*b)
            elif operation == "/": stack.append(int(a/b))

        return stack[0]