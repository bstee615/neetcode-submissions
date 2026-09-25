class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        j = 0
        m = 0
        while j < len(s):
            while s[j] in seen:
                seen = seen - {s[i]}
                i += 1
            seen.add(s[j])
            m = max(m, j - i + 1)
            j += 1
        return m
