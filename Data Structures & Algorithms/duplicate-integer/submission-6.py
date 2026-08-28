class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = defaultdict(int)
        for i in nums:
            if i not in check:
                check[i] += 1
            elif i in check:
                return True
        return False



        