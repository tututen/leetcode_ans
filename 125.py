import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = re.sub(r'[^a-z0-9]+', '', s.lower())
        return v == v[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("0P"))
