class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphaMap = {} 

        if len(magazine) < len(ransomNote):
            return False

        for c in range(len(magazine)):
            char = magazine[c]
            key = ord(char) - ord("a")
            if key not in alphaMap:
                alphaMap[key] = 0
            alphaMap[key] += 1

        for i in range(len(ransomNote)):
            char = ransomNote[i]
            key = ord(char) - ord("a")
            if key not in alphaMap:
                return False
            alphaMap[key] -= 1
            if alphaMap[key] < 0:
                return False
            
        return True
            