import copy
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answers = set()
        self.n = n
        self.add("", 0, 0)
        return self.answers
    def add(self, current, left, right):
        if left == right and left == self.n:
            self.answers.add(current)
            return
        elif left == self.n:
            self.add(copy.deepcopy(current) + ")", copy.deepcopy(left), copy.deepcopy(right) + 1)
        elif left == right:
            self.add(copy.deepcopy(current) + "(", copy.deepcopy(left) + 1, copy.deepcopy(right))
        else:
            self.add(copy.deepcopy(current) + "(", copy.deepcopy(left) + 1, copy.deepcopy(right))
            self.add(copy.deepcopy(current) + ")", copy.deepcopy(left), copy.deepcopy(right) + 1)
    