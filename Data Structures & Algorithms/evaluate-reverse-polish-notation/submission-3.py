class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ["+", "-", "*", "/"]

        for char in tokens:
            if char not in operators:
                stack.append(int(char))

            else:
                char2 = stack.pop()
                char1 = stack.pop()

                if char == "+":
                    result = char1 + char2
                elif char == "-":
                    result = char1 - char2
                elif char == "*":
                    result = char1 * char2
                else:
                    result = int(char1 / char2)

                stack.append(result)

        return stack[0]
