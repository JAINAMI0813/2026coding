#week04-4a.py (重寫week04-2.py)
#Leetcode 1732. Find the Highest Altitude
#找到最高海拔高度
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain)
        ans = H = 0 #一開始高度是0
        for gg in gain:
            H += gg
            ans = max(ans,H)
        return ans
