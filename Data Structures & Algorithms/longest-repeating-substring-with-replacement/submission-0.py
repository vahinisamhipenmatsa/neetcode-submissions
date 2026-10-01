class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        j = 0

        curr_hash_map = {}
        max_length = 0

        while j < len(s):
            curr_hash_map[s[j]] = curr_hash_map.get(s[j], 0) + 1
            max_value = max(curr_hash_map.values())
            # see if we reach the k yet or not until we do we wanna keep expanding j in the window
            while (j - i + 1) - max_value > k:
                curr_hash_map[s[i]] -= 1
                i += 1
            max_length = max(max_length, j - i + 1)
            j += 1
        return max_length
