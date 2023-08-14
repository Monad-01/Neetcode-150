class Solution:
    

    def isPalindrome(self, s: str) -> bool:

        fp = 0
        lp = len(s) - 1

        while fp < lp:
            #Checking First Character
            if self.isValidChar(s[fp]):
                #Checking Second Character
                if self.isValidChar(s[lp]):
                    #If both are valid then do equivalency check
                    if s[fp].lower() == s[lp].lower():
                        fp += 1
                        lp -= 1
                        continue
                    else:
                        return False
                else:
                    lp -= 1
            else:
                fp += 1
            

            
        return True

    def isValidChar(self,c):
            return (
                ord("A") <= ord(c) <= ord("Z")
                or ord('a') <= ord(c) <= ord('z')
                or ord("0") <= ord(c) <= ord("9")
            )

        