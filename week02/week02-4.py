#week02-4.py 學習計畫 第三題
#LeetCode 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i,j = 0,len (height)-1 #左邊i 右邊j
        while i<j:#只要左右還沒撞在一起
            area = (j-i) * min(height[i],height[j])#算出現在的面積
            ans = max(ans,area)
            if height[i] < height[j]: i += 1
            else: j -= 1 #小的j,往左
        return ans
