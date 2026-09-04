class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = ""

        for char in s.lower():
            if char.isalnum():
                new += char

        return new == new[::-1]