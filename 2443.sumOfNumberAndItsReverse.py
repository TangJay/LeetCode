class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        for i in range(num // 2, num):
            length = len(str(i))
            if (i % 10 + i // (10 ** (length - 1))) % 10 == num % 10:
                rev = self.reverse(i)
                if rev + i == num:
                    return True
        return False 
    def reverse(self, num):
        S = str(num)
        ret = 0
        for i in range(len(S) - 1, -1, -1):
            ret += 10 ** i * int(S[i])
        return ret