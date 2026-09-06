class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        new = ''.join(ch for ch in s if ch.isalnum())

        return new == new[::-1]