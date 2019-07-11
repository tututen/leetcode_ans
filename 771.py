class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = 0
        for j in J:
            c += S.count(j)
        return c
