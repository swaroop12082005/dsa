class Solution(object):
    def backspaceCompare(self, s, t):

        def convert(text):
            ans = ""

            for ch in text:
                if ch == "#":
                    ans = ans[:-1]
                else:
                    ans += ch

            return ans

        return convert(s) == convert(t)