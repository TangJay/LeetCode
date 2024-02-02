class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numslist = nums1 + nums2
        numslist.sort()
        number = (len(numslist) - 1) / 2
        if number % 1 == 0:
            return numslist[int(number)]
        else:
            return (numslist[int(number - 0.5)] + numslist[int(number + 0.5)]) / 2
