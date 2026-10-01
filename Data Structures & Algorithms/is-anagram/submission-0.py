class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams mean they have teh same characters and number of characters
        
        # ensuring cases wont affect anything
        s = s.lower()
        t = t.lower()

        # ensuring the lengths are the same before doing anything else
        if len(s) != len(t):
            return False

        # make a dict add for s count and remove for t count
        # if any value is not zero than we return False
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        for c in t:
            if c in s_dict:
                if s_dict[c] < 1:
                    return False
                s_dict[c] -= 1
            else:
                return False
        return True


        