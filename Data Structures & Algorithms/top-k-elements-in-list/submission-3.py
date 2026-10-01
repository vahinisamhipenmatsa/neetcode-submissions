class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # here we are populatin our hashmap
        frequency = {}
        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)
        


        # use min heap approach
        import heapq
        min_heap = []
        for key,value in frequency.items():
            # this will soert by value (aka freq) first which we want
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                # this gets rid of the smallest elements
                # want to ensure that we are only keeping k elements in the list
                heapq.heappop(min_heap)

        # returning value instead of keeping the pairs like before
        return [key for value,key in min_heap]
        
        
        
        
        

        







        

        