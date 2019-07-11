from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        nums.append(None)  # block
        # print(nums)
        while len(nums) > 0:
            # print(nums[0], nums[1])
            if nums[0] != nums[1]:
                return nums[0]
            del nums[0]
            del nums[0]


print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
