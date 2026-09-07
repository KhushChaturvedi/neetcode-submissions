class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pair.append((position[i], time))

        pair.sort(reverse=True)

        stack = []

        for i in pair:
            if not stack or i[1] > stack[-1]:
                stack.append(i[1])

        return len(stack) 