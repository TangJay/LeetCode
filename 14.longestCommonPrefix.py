class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = []
        end = 0
        same = True
        for i in strs:
            lens.append(len(i))
        for i in range(min(lens)):
            end = i + 1
            basic = strs[0][:i + 1]
            for j in strs:
                if j[:i + 1] != basic:
                    same = False
                    break
            if same == False:
                break
        if same == True:
            if end != 0:
                return strs[0][:end]
            else:
                return ""
        return strs[0][:end - 1]