class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L, length = 0,0
        for R in range(len(s)):
            while s[R] in s[L:R]:
                L += 1
            length = max(length, len(s[L:R + 1]))
        
        return length

