class Solution:
    def trap(self, height: List[int]) -> int:
        # we have to keep track of the maximum left height 
        # and keep track of maximimu right heigh
        # so at the current position we can 

        # hash map of max left and right
        max_left = 0
        max_right = 0
        hash_map_left = {}
        hash_map_right = {}

        for i in range(len(height)):
            hash_map_left[i] = max_left

            max_left = max(height[i], max_left)
        
        for i in range(len(height) - 1, -1, -1):
            hash_map_right[i] = max_right
            max_right = max(height[i], max_right)

        print(hash_map_left)
        print(hash_map_right)
        
        # now that we have set up the hash amap we can loop through array and calculate height

        area = 0

        for i in range(len(height)):
            current = min(hash_map_left[i], hash_map_right[i]) - height[i]
            
            if current > 0: # avoids dealign with negative numbers which may appear due to our equation
                area += current 
        return area
        


