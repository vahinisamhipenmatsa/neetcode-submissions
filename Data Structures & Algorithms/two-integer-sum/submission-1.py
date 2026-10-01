class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_set = {}
        for j in range(len(nums)):
            needed = target - nums[j]
            if needed in hash_set:
                return [hash_set[needed], j]
            hash_set[nums[j]] = j
        return [-1,-1]
