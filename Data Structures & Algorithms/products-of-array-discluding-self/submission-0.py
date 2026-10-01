class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix suffic approach
        prefix = 1
        suffix = 1
        prefix_lst = [0] * len(nums)
        suffix_lst = [0] * len(nums) 

        # setting up the prefix products
        for i in range(len(nums)):
            prefix_lst[i] = prefix
            # add in prefix for future work
            prefix *= nums[i]
        
        # setting up suffix list
        for i in range(len(nums) - 1, -1, -1):
            # iterating from right to left
            suffix_lst[i] = suffix
            suffix *= nums[i]
        
        # now final list which multiplies the two together
        final_lst = []
        for i in range(len(nums)):
            product = prefix_lst[i] * suffix_lst[i]
            final_lst.append(product)
        return final_lst


            
        