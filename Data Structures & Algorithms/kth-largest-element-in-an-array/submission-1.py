class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

    
        """
        sorting the array, then iterating and returning i = k -1
        O(n log n) - time complexity 
        O(n) - space complexity

        
        """

        track = [-x for x in nums]

        heapq.heapify(track)

        for i in range(k-1):
            heapq.heappop(track)
        
        return -(heapq.heappop(track))
        