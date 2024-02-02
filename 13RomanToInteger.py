class Solution:
    def romanToInt(self, s: str) -> int:
        change = [["M", "D", "C", "L", "X", "V", "I"], [1000, 500, 100, 50, 10, 5, 1]]
        ans = 0
        times = 1
        place = change[0].index(s[0]) 
        for i in s[1:]:
            if change[0].index(i) < place:
                times = 0
                ans -= change[1][place]
                a = 2 * change[1][place]
                place = change[0].index(i) 
                ans += change[1][place]
            else:
                ans += times * change[1][place]
                place = change[0].index(i) 
                times = 1
        if times >= 1:
            ans += change[1][place]
        return ans