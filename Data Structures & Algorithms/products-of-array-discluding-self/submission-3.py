class Solution:
    # space: O(n)
    # time: O(n) but O(1) if we dont want to include the return value
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1 
        suffix = 1

        final = []

        # lets first get it in O(n) then optimize to be in one loop

        # just doing the prefixes first
        for num in nums:
            final.append(prefix)
            prefix *= num


        for i in range(len(nums) - 1, -1, -1):
            # now oing in reverse to do suffix
            final[i] *= suffix
            suffix *= nums[i]
        
        return final
