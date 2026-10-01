class Solution:
    # now we have to figure out a way to reduce the space complexity
    def trap(self, height: List[int]) -> int:
        # we have to keep track of the maximum left height 
        # and keep track of maximimu right heigh
        # so at the current position we can 


        l = 0
        r = len(height) - 1

        max_left = height[l]
        max_right = height[r]

        total_area = 0

        while l < r:
            if max_left <= max_right:
                # this is the minimumk which is what we want
                l += 1 
                max_left = max(max_left, height[l])
                
                current = max_left - height[l]
                if current > 0:
                    total_area += max_left - height[l]
            else:
                # we can assume that the minimum is on the right side
                r -= 1
                max_right = max(max_right, height[r])


                current = max_right - height[r]
                if current > 0:
                    total_area += max_right - height[r]
        return total_area



        # # hash map of max left and right
        # max_left = 0
        # max_right = 0
        # hash_map_left = {}
        # hash_map_right = {}

        # for i in range(len(height)):
        #     hash_map_left[i] = max_left

        #     max_left = max(height[i], max_left)
        
        # for i in range(len(height) - 1, -1, -1):
        #     hash_map_right[i] = max_right
        #     max_right = max(height[i], max_right)
        
        # area = 0

        # for i in range(len(height)):
        #     current = min(hash_map_left[i], hash_map_right[i]) - height[i]
            
        #     if current > 0: # avoids dealign with negative numbers which may appear due to our equation
        #         area += current 
        # return area
        


