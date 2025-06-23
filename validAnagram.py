class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        for i in range(len(s)):
            if s[i] in maps:
                maps[s[i]] += 1
            else:
                maps[s[i]] = 0
        maps2 = {}
        for i in range(len(t)):
            if t[i] in maps2:
                maps2[t[i]] += 1
            else:
                maps2[t[i]] = 0
        return (maps == maps2)