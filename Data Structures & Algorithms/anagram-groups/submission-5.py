class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            s = ''.join(sorted(word))
            groups[s].append(word)
        
        return list(groups.values())
        