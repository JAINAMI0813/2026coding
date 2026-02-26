#week01-5.py學習計畫 array/string 第7題
#Leetcode 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)#陣列的長度
        preSum = [1]
        postSum = [1]
        for i in range(N):
            preSum.append(preSum[-1]*nums[i])
            postSum.append(postSum[-1]*nums[N-1-i])
            print(postSum)
        ans = []
        for i in range(N):
            ans.append(preSum[i]*postSum[N-1-i])#左邊累積 + 右邊累積
        return ans
