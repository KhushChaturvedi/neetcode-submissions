class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        set_nums = set(nums)
        best = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                current = num

                while current + 1 in set_nums:
                    current += 1
                    length += 1

                if length > best:
                    best = length

        return best