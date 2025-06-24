class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        first, second = 0, 1
        currCount = 1
        letters = set()
        letters.add(s[first])
        while (second < len(s)):
            if s[second] not in letters:
                letters.add(s[second])
                currCount = max(currCount, len(letters)) # checks if window size has gotten bigger
                second += 1
            else:
                letters.remove(s[first])
                first += 1
                print('changing')
            print(first, second)
        return currCount