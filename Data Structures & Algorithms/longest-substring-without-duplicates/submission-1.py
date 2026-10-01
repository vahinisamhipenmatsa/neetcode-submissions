class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length of longest substring without duplicate characters
        curr_set = set()
        i = 0
        j = 0
        max_len = 0
        while j < len(s):
            while s[j] in curr_set:
                curr_set.remove(s[i])
                i += 1
            curr_set.add(s[j])
            j += 1

            max_len = max(max_len, len(curr_set))
        return max_len


        

        


        