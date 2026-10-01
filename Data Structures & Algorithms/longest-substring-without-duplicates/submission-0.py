class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring without duplicate characters
        



        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            # this represents s
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


        