class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements
        # first lets have a dict with the number of frequencies
        dict_nums = {}
        for n in nums: 
            dict_nums[n] = dict_nums.get(n,0) + 1 
        
        # pick k keys with highest values
        # we can use a heap to do this that is the size of k
        import heapq
        heap = [] # this is min heap 
        for key,value in dict_nums.items(): # O(n)
            heapq.heappush(heap, (value, key)) # O(log k)

            if len(heap) > k:
                heapq.heappop(heap)
        # now we can just return the outputted numbers easily
        return [num for f, num in heap]

# when you here frequency or k numbers doing something automatically think heap
# time compelxity: O(n log k)
# space complexity: O(n)







        

        