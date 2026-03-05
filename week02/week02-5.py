#week02-5.py 學習計畫 第四題
#LeetCode 1679. Max Number of K-Sum Pairs
#希望找到「加起來==K」
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()#小到大排好，等一下「左挑1，右挑1」看能不能組合
        ans = 0
        i, j = 0,len(nums) -1
        while i < j:
            if nums[i] + nums[j] == k:
                ans += 1
                i,j = i+1,j-1 #右邊用了 往右
            if nums[i] + nums[j] < k:
                i = i+1
            if nums[i] + nums[j] > k:
                j = j-1
        return ans
