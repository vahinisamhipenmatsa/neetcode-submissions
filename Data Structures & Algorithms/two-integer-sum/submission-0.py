class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in sums:
                return [sums[needed], i]
            # now we add to dict in case it wasnt there before
            sums[nums[i]] = i
        return [0,0]

        # time complexity: O(n) for the for loop for the list
        # space complexity: O(n) for the dictionary (hash map)

        