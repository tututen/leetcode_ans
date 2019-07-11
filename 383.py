class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ms = [c for c in magazine]
        for r in ransomNote:
            ss = ''.join(ms)
            if ss.find(r) == -1:
                return False
            ms.remove(r)
        return True


print(Solution().canConstruct("aa", "ab"))
