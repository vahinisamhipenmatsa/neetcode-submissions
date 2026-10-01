class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # true if value appears more than once
        # false otherwise
        counts = []
        for value in nums:
            if value in counts:
                return True
            counts.append(value)
        return False
        
        