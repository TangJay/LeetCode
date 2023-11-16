class Solution:
    def myAtoi(self, s: str) -> int:
        reverse = False
        s = s.strip()
        if len(s) == 0:
            return 0
        positive = False
        negative = False
        typed = False
        while True:
            print(s)
            if s[0] == "-" or s[0] == "+":
                if typed == True:
                    return 0
                typed = True
                if s[0] == "-":
                    reverse = True
                s = s[1:]
            else:
                break
            if len(s) == 0:
                return 0

        if s[0].isnumeric() == False:
            return 0
        for i in range(len(s)):
            print(s[i])
            if s[i].isnumeric() == False:
                print("0")
                s = s[0:i]
                break
        print(reverse)
        if int(s) >= 2**31:
            if reverse == True:
                s = 2**31
            else:
                s = 2**31 - 1
        if reverse == True:
            return -1 * int(s)
        return int(s)
