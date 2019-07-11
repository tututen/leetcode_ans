from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if str(n) in d:
                d[str(n)] += 1
            else:
                d[str(n)] = 1
        max_count = max(d.values())
        print([int(k) for k, v in d.items() if v == max_count])
        print(d)
        return sum([int(k) for k, v in d.items() if v == max_count])


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
