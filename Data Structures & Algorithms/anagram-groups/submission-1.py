class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set1=defaultdict(list)
        for s in strs:
            stored="".join(sorted(s))
            set1[stored].append(s)
        return list(set1.values())




        