class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_strs = defaultdict(list)
        for i, s in enumerate(strs):
            sorted_strs[tuple(sorted(s))].append(i)
        grouped_strs = []
        for key, indices in sorted_strs.items():
            l = []
            grouped_strs.append(l)
            for i in indices:
                l.append(strs[i])
        return grouped_strs