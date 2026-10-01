class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # search the indices of two numbers os they addd to target
        # and oindex 1 is less than index 2

        i = 0
        j = len(numbers) - 1

        while i < j:
            value = numbers[j] + numbers[i]
            if value == target:
                return [i + 1, j + 1]
            elif value < target:
                # value needs to be bigger 
                i += 1
            else:
                # value needs to be smaller
                j -= 1
        return [-1,-1]


        # space is O(1)
        # time is o(n)


        