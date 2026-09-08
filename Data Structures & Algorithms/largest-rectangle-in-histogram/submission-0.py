from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and stack[-1][1] > h:
                popped_index, popped_height = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1][0] - 1
                maxArea = max(maxArea, popped_height * width)
            stack.append((i, h))

        while stack:
            popped_index, popped_height = stack.pop()
            if not stack:
                width = len(heights)
            else:
                width = len(heights) - stack[-1][0] - 1
            maxArea = max(maxArea, popped_height * width)

        return maxArea