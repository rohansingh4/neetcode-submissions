class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "/", "*"}:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                match token:
                    case "+":
                        result = left + right
                    case "-":
                        result = left - right
                    case "*":
                        result = left * right
                    case "/":
                        result = left / right
                stack.append(int(result))
        return stack[-1]