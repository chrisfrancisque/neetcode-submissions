class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr = 0 
        res = 0
        prefix = {0:1} # prefixSum: count 

        for num in nums:
            curr += num 
            diff = curr - k

            if diff in prefix:
                res += prefix[diff]
        
            if curr in prefix:
                prefix[curr] += 1
            else:
                prefix[curr] = 1
            
        
        return res
                
        