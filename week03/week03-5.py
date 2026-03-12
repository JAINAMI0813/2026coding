#week03-5.py 學習計畫
#LeetCode 1493. Longest Subarray of 1's After Deleting One Element
#陣列裡 一定要刪掉1個 問剩下的陣列裡 最長的一有幾個

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        zeros =0
        tail = 0
        ans = 0
        for head in range(N):#逐一往右吃
            if nums[head]==0: zeros += 1
            while zeros > 1: #有毒的0 太多了
                if nums[tail]==0: zeros -= 1
                tail += 1#尾巴吐之後右縮
            ans = max(ans,head - tail + 1)
        return ans - 1
