class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagrams together i guess
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        # now we need to get all of the lsist of teh dictionary
        final_list = []
        for key in anagrams:
            final_list.append(anagrams[key])
        return final_list

        