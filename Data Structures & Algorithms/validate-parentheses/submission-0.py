class Solution:
    def isValid(self, s: str) -> bool:
        # haver a stack and add 


        matching = {")": "(", "}": "{", "]": "["}

        stack = []
        for char in s:
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack == []:
            return True
        else:
            return False
            

