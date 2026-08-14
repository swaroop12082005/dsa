class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = "".join([char.lower() for char in s if char.isalnum()])
    
        return check == check[::-1]
        