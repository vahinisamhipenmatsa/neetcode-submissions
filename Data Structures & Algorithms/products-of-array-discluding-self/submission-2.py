class Solution:
    # space: O(n)
    # time: O(n) + O(n) + O(n) = O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix suffic approach
        prefix = 1
        suffix = 1
        prefix_lst = [1] * len(nums)

        # setting up the prefix products
        for i in range(len(nums)):
            prefix_lst[i] = prefix
            # add in prefix for future work
            prefix *= nums[i]
        
        # setting up suffix list
        for i in range(len(nums) - 1, -1, -1):
            # iterating from right to left
            prefix_lst[i] *= suffix
            suffix *= nums[i]
        
        return prefix_lst


            
        