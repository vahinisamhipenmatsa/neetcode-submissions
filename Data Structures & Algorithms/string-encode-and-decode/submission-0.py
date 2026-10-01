class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode it 
        result = ""
        for s in strs:
            # looping through each string
            result += str(len(s)) + "#" + s 
        return result

        # this way before hashtag we know how many letters for each one

    def decode(self, s: str) -> List[str]:
        # decodes it
        result = []
        i = 0
        while i < len(s):
            j = i

            # we want to isolate the number so we can get the string
            while s[j] != "#":
                j += 1 
            # we have now isoalted it
            num = int(s[i:j])

            # now this is the number we use to append to result
            i = j + 1 
            j = i + num 
            result.append(s[i:j])

            # now move pointer forwatd
            i = j
        return result




            
