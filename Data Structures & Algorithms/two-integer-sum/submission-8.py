class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        tracker = {}

        for i, n in enumerate(nums):
            curr = target - n

            if curr in tracker:
                return [tracker[curr], i]
            
            tracker[n] = i
        
        return [0,0]
        