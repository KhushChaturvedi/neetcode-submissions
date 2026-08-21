class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        totalwater = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    totalwater += leftmax - height[left]

                left += 1

            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    totalwater  += rightmax - height[right]
                right -= 1

        return totalwater