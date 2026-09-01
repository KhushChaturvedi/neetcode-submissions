class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        need = len(count_t)
        have = 0

        windows_count = {}
        left = 0
        result = ""
        result_len = float('inf')

        for right in range(len(s)):
            char = s[right]
            windows_count[char] = windows_count.get(char, 0) + 1

            if char in count_t and windows_count[char] == count_t[char]:
                have += 1

            while have == need:
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                windows_count[left_char] -= 1
                if left_char in count_t and windows_count[left_char] < count_t[left_char]:
                    have -= 1

                left += 1

        return result