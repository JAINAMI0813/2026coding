#week04-5.py 學習計畫 第二題
#LeetCode 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N =len(nums)
        prefix = [0]#一開始 prefix sum 只有一個[0]
        for i in range(N):
            prefix.append(prefix[-1]+nums[i])#陣列變長了
        #print(prefix)
        postfix = [0] * (N+1)
        for i in range(N-1,-1,-1):
            postfix[i] = postfix[i+1] + nums[i]
            if prefix[i] == postfix[i+1]:return i
        #print(postfix)
        return -1
