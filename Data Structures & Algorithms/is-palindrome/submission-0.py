class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()
        return True if t == t[::-1] else False
        
