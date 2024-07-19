class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            ans.append(-1)
            if nums2.index(i) == len(nums2):
                continue
            for j in nums2[nums2.index(i) + 1 : ]:
                if j > i:
                    ans.pop()
                    ans.append(j)
                    break
        return ans