class Solution:
    def sortedSquares(self, nums):
        ans = []

        for i in nums:
            ans.append(i * i)

        ans.sort()

        return ans
        