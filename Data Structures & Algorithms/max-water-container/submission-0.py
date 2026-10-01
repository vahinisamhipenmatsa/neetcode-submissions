class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer approach

        i = 0
        j = len(heights) - 1 

        max_water = 0
        while i < j:
            first = heights[i]
            second = heights[j]

            if first >= second:
                area = second * (j - i)
                # we move second 
                j -= 1
            else:
                area = first * (j - i)
                # we move first
                i += 1
            if area > max_water:
                max_water = area
        
        # need to figure out when is the best time to move the pointers
        return max_water
        