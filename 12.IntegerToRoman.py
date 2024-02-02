class Solution:
    def intToRoman(self, num: int) -> str:
        self.switch = [
            ["I", 1],
            ["V", 5],
            ["X", 10],
            ["L", 50],
            ["C", 100],
            ["D", 500],
            ["M", 1000],
        ]
        romans = []
        romans.append("M" * (num // 1000))
        for i in range(4, -1, -2):
            romans.append(self.calculate(num, i))
        result = ""
        for i in romans:
            result += i
        return result

    def calculate(self, num, turn):
        print(turn)
        num = num % self.switch[turn + 2][1]
        amount = num // self.switch[turn][1]
        print(amount)
        if amount == 4:
            return self.switch[turn][0] + self.switch[turn + 1][0]
        elif amount == 9:
            return self.switch[turn][0] + self.switch[turn + 2][0]
        elif amount >= 5:
            return self.switch[turn + 1][0] + self.switch[turn][0] * (amount - 5)
        else:
            return self.switch[turn][0] * (amount)
