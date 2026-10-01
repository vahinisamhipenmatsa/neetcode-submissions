class Solution:

    def encode(self, strs: List[str]) -> str:
        # need to bne encoded into a single string
        single_str = ""

        # since delimeter can pop up in the word
        for word in strs:
            single_str += str(len(word))
            single_str += ","
        single_str += "#"

        for word in strs:
            single_str += word
    
        return single_str

    def decode(self, s: str) -> List[str]:
        #first we need to find the numbers
        i = 0
        j = 0 
        sizes = []
        while s[i] != '#':
            # we will continue finding the numbers we need for the words
            j = i 
            while s[j] != ',':
                j += 1
            
            number = s[i:j]
            sizes.append(int(number))
            i = j + 1
        
        # now we need to go through these sizes starting off with after the pound size
        i += 1 # since whiel loop exits when it is the pound sign

        result = []
        for size in sizes:
            word = s[i:i+size]
            result.append(word)
            i += size

        return result


        





        


            
