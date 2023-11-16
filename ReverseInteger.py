class Solution:
    def reverse(self, x: int) -> int:
        if 10 > abs(x):
            return x
        index = []
        power = 0
        while True:
            number = abs(x) // int(10**power) % 10
            print(number)
            if 10**power > abs(x):
                break
            else:
                index.append(str(number))
            power += 1
        print(index)
        result = int("".join(index))
        if result >= 2**31:
            return 0
        if x >= 0:
            return result
        else:
            return -1 * result
