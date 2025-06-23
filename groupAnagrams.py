class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        group = []
        for i in strs:
            letters = [0] * 26
            for j in i:
                letters[ord(j) - ord('a')] += 1
            grams[tuple(letters)].append(i)
        
        for v in grams.values():
            group.append(v)
        
        return group
        
