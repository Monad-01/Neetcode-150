class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = [*s]
        t = [*t]
        for letter in s:
            if letter in t:
                t.remove(letter)
            else:
                return False
        return True
