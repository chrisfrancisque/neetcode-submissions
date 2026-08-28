class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sin = set()

        for n in nums:
            if n not in sin:
                sin.add(n)
            elif n in sin:
                return True
        
        return False
        