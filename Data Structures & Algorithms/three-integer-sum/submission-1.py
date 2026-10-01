class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort() # need to make sure the list is sorted
        # loop through i and figure out pairs for j and k (what you need)
        for i in range(len(nums) - 2):
            # skipping duplicate i's 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            remaining = -1 * nums[i]

            # from here we do two pointer approach
            j = i + 1 # left pointer 
            k = len(nums) - 1 # right pointer
            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum > remaining:
                    k -= 1
                elif two_sum < remaining:
                    j += 1
                else:
                    final.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                    
        return final








            
        