class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # auto return based on length
        if len(nums) < 2:
            return len(nums)

        # getting sorted unique elements to avoid duplicates
        nums = sorted(set(nums))

        max_seq = 1
        current = 1
        past = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == past + 1:
                current += 1
            else:
                current = 1

            max_seq = max(max_seq, current)

            past = nums[i]

        return max_seq


        