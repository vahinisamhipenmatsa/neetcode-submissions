class Solution:
    # space: O(n)
    # time: O(n) but O(1) if we dont want to include the return value
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        suffix = 1
        final = [1] * len(nums)

        i = 0
        j = len(nums) - 1 



        for i in range(len(nums)):
            final[i] *= prefix
            prefix *= nums[i]


            # another way to do j
            final[-1 - i] *= suffix
            suffix *= nums[-1 - i]
        
        return final