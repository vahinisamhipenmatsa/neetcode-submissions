class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            if n in frequency:
                frequency[n] += 1
            else:
                frequency[n] = 1
        


        # now need a way to find the k most frequent items

        # want to keep max here somehow
        import heapq
        min_heap = []
        for key,value in frequency.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                # this gets rid of the smallest elements
                heapq.heappop(min_heap)
        
        return [key for value,key in min_heap]
        
        
        
        
        

        







        

        