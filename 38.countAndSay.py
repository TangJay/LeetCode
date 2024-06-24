class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        for i in range(n - 1):
            last = num[0]
            times = 0
            temp = ""
            for i in num:
                if i != last:
                    temp += f"{times}{last}"
                    times = 1
                    last = i
                else:
                    times += 1
            temp += f"{times}{last}"
            num = temp
        return num