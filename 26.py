from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = sorted(set(nums))
        nums.clear()
        nums.extends(l)
        return len(l)
