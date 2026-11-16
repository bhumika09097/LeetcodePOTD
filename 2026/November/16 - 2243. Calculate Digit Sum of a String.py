class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            groupSum = 0
            length = 0
            for i in range(len(s)):
                groupSum += int(s[i])
                length += 1
                if length == k:
                    length = 0
                    new_s += str(groupSum)
                    groupSum = 0
            if length > 0:
                new_s += str(groupSum)

            s = new_s

        return s
