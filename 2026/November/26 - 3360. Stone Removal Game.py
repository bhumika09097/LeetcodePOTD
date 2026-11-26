class Solution:
    def canAliceWin(self, n: int) -> bool:
        removeablestones = 10
        turns = 0
        while n >= removeablestones:
            n -= removeablestones
            removeablestones -= 1
            turns += 1

        if turns % 2 != 0:
            return True
        
        return False

