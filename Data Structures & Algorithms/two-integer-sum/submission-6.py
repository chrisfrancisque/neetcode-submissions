class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        compliment = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in compliment:
                return [compliment[comp], i]
            
            compliment[num] = i
        
        return []
        