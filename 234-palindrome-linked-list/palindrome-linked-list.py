
class Solution:
    def isPalindrome(self, head):

        values = []

        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values == values[::-1]