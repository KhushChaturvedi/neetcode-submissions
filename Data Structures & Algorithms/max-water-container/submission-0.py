class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(heights[left],heights[right])
            area = width * current_height

            if max_area < area:
                max_area = area

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            elif heights[left] == heights[right]:
                left += 1   

        return max_area
