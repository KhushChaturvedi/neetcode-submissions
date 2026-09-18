class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            left1 = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            right1 = nums1[partitionX] if partitionX < m else float('inf')

            left2 = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            right2 = nums2[partitionY] if partitionY < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = partitionX - 1
            else:
                left = partitionX + 1