class Solution:
    def isPalindrome(self, s: str) -> bool:
        # need to lower case and make sure it is alpha


        # now we need to check if both are the same
        i = 0
        j = len(s) - 1

        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1 
                continue

            # check that they are same 
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
                
        