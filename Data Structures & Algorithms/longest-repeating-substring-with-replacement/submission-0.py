class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        count = {}
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            max_freq = max(max_freq, count[char])

            while right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length , right - left + 1)

        return max_length