#week03-4.py 學習計畫 sliding window 第二題
#Leetcode 1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0 #一開始的蛇 沒有0
        N = len(nums)
        ans = 0
        tail = 0 #尾巴一開始黏在0的位置 只有拉肚子 才會往右縮
        for head in range(N):#慢慢往右吃
            if nums[head]==0:
                zeros +=1
                while zeros > k:#愛用 while 迴圈，一直拉肚子
                    if nums[tail]==0:
                        zeros -=1 #毒素減少
                    tail += 1
            ans = max(ans,head - tail + 1)
        return ans #最長的 不會中毒而死的蛇蛇 長度是ans
