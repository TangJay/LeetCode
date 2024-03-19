import copy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.trans = {"2" : ["a", "b", "c"], "3" : ["d", "e", "f"], "4" : ["g", "h", "i"], "5" : ["j", "k", "l"], "6" : ["m", "n", "o"], "7" : ["p", "q", "r", "s"], "8" : ["t", "u", "v"], "9" : ["w", "x", "y", "z"]}
        self.digits = digits
        self.ans = []
        if len(self.digits) >= 1:
            self.add(0, "")
        return self.ans
    def add(self, turn, letters):
        print(self.trans[self.digits[turn]])
        for i in self.trans[self.digits[turn]]:
            if turn == len(self.digits) - 1:
                self.ans.append(copy.deepcopy(letters) + i)
            else:
                print(turn)
                self.add(turn + 1, copy.deepcopy(letters) + i)
        return
            