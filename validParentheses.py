class Solution:
    def isValid(self, s: str) -> bool:
        pairs = []
        starts = "{(["
        duo = {'}': '{', ')': "(", "]": "["}
        for i in s:
            if i in starts:
                pairs.append(i)
            elif len(pairs) == 0:
                return False
            elif pairs.pop() != duo[i]:
                return False
        if len(pairs) == 0:
            return True
        return False