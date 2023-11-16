class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        splitted = list(s)
        oks = []
        amount = [0]
        times = 0
        for i in range(len(splitted)):
            if splitted[i] in oks:
                del oks[0 : oks.index(splitted[i]) + 1]
            oks.append(splitted[i])
            amount.append(len(oks))
        return max(amount)
