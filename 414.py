from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ns = list(set(nums[:]))
        if len(ns) < 3:
            return max(ns)
        for _ in range(2):
            ns.remove(max(ns))
        return max(ns)
