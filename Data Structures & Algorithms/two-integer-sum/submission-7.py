class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = dict()

        for i, num in enumerate(nums):
            curr = target - num
            if curr in res:
                return [res[curr], i]
            
            res[num] = i
        
            
        