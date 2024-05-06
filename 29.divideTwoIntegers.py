class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = 0
        if divisor <= 0:
            divisor = 0 - divisor
            negative = 1 - negative
        if dividend <= 0:
            dividend = 0 - dividend
            negative = 1 - negative
        self.divisor = divisor
        dividend = str(dividend)
        ans = ""
        last = 0
        for i in dividend:
            times, last = self.count(10 * last + int(i))
            ans += str(times)
        if negative == 1:
            return 0 - int(ans)
        if int(ans) == 2147483648:
            return 2147483647
        return int(ans)
    def count(self, req):
        times = 0
        while True:
            if req >= self.divisor:
                times += 1
                req -= self.divisor
            else:
                return times, req