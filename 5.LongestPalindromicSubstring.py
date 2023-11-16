import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        places = dict()
        ans = ""
        for i in range(len(s)):
            for j in range(2):
                if i == len(s) - 1 and j == 1:
                    break
                ans = self.judgeMiddle(s, i, i + j, ans)
        """ 
        for i in range(len(s)):
            if s[i] not in places:
                places[s[i]] = self.getSame(s, i)
            else:
                characterList = places[s[i]]
                del characterList[0 : 2]
                characterList.insert(0, characterList[0])
            for j in range(1, len(places[s[i]])):
                if len(s[i : places[s[i]][j] + 1]) > len(ans):
                    TF = self.judge(s[i : places[s[i]][j] + 1])
                    if TF == True:
                        ans = s[i : places[s[i]][j] + 1]
                else:
                    continue
        """
        return ans

    def getSame(self, slist, index):
        sameList = [index]
        for i in range(len(slist)):
            if slist[i] == slist[index]:
                sameList.append(i)
        return sameList

    def judge(self, slist):
        for i in range(0, int(len(slist) / 2)):
            if slist[i] != slist[len(slist) - i - 1]:
                return False
        return True

    def judgeMiddle(self, s, start, end, ans):
        i = 0
        while True:
            if s[start - i] != s[end + i]:
                return ans
            if (end + i) - (start - i) + 1 > len(ans):
                ans = s[start - i : end + i + 1]
            if start - i == 0 or end + i == len(s) - 1:
                return ans
            i += 1
