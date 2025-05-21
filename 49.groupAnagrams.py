import copy


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.dict = {}
        for i in range(len(strs)):
            temp = []
            for j in strs[i]:
                temp.append(j)
            temp.sort()
            string = "".join(temp)
            if string in self.dict:
                self.dict[string].append(i)
            else:
                self.dict[string] = [i]
        print(self.dict)
        ans = []
        for i in self.dict:
            print(i)
            temp = []
            for j in self.dict[i]:
                temp.append(strs[int(j)])
            ans.append(temp)
        return ans
