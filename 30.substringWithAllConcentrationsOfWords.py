import copy
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        end = []
        if len(set(words)) == 1 and len(set(s)) == 1 and len(s) >= len(words):
            temp = dict(Counter(words))
            amount = 0
            for k in temp.keys():
                amount += len(k) * temp[k]
            end = list(range(len(s) - amount + 1))
            return end
        for i in set(words):
            ret = self.find(s, i)
            for res in ret:
                L = copy.deepcopy(words)
                L.remove(i)
                if self.check(s, res + len(i), L) == True:
                    end.append(res)
        return end
    def find(self, string, word):
        ret = []
        for i in range(len(string) - len(word) + 1):
            if string[i : i + len(word)] == word:
                ret.append(i)
        return ret
    def check(self, string, start, words):
        for i in words:
            if string[start : start + len(i)] == i:
                words.remove(i)
                start += len(i)
                ans = self.check(string, start, words)
                return ans
        if len(words) == 0:
            return True
        else:
            return False