#week05-2a.py 學習計畫先寫最慢的版本
#Leetcode 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1,nums2 = set(nums1),set
        ans1 = []#放「在nums1但不在nums2」的數
        for num in nums1:#逐一取出
            if num not in nums2:
                ans1.append(num)
        ans2 = []
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return[list(set(ans1)),list(set(ans2))]
