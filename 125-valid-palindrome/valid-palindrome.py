class Solution:
    def isPalindrome(self, s): 

        ans = []

        for ch in s:
            if ch.isalnum():
                ans.append(ch.lower())

        clean = "".join(ans)

        return clean == clean[::-1]