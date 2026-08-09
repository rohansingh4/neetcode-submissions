class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
            
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != close_to_open[ch]:
                    return False
                stack.pop()
        return True if not stack else False