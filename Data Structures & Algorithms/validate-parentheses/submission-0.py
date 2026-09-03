class Solution:
    def isValid(self, s: str) -> bool:
        
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            if char in matches:
                if stack == [] or stack[-1] != matches[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return stack == []