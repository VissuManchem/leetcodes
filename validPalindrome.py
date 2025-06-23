class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        second = len(s)-1
        while(first <= second):
            if s[first].isalnum() == False:
                first += 1
            elif s[second].isalnum() == False:
                second -= 1
            elif s[first].lower() != s[second].lower():
                return False
            else:
                first += 1
                second -= 1
        return True