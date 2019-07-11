from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        i = 1
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(s) for s in strs])
        while i <= min_len:
            ss = {s[:i] for s in strs}
            if len(ss) != 1:
                return ret
            ret = ss.pop()
            i += 1
        return ret


Solution().longestCommonPrefix([""])
