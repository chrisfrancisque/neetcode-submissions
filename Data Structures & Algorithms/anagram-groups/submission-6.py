class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            curr = ''.join(sorted(word))
            ans[curr].append(word)
        return list(ans.values())

        