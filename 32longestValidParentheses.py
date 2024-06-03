class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lefts = []
        confirm = []
        for i in range(len(s)):
            if s[i] == "(":
                lefts.append(i)
            else:
                if len(lefts) == 0:
                    continue
                confirm.append(i)
                confirm.append(lefts.pop())
        confirm.sort()
        last = 0
        ans = [0]
        for i in range(1, len(confirm)):
            if confirm[i] - confirm[i - 1] != 1:
                last = i
            else:
                ans.append(i - last + 1)
        return max(ans) 