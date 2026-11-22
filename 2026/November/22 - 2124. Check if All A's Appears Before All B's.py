class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        see_b = False
        for i in range(n):
            if s[i] == 'b':
                see_b = True
            if s[i] == 'a' and see_b:
                return False

        return True 
