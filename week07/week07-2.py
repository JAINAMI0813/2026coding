#week07-2.py 學習計畫stack 第二題
#Leetcode 735. Asteroid Collision
#正得向左、負的向左 大的會把小的消滅 一樣大 一起死
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a>0:
                ans.append(a)#直接塞
            else:#負往左，可能會跟 ans裡的東西相撞很多次
                while ans and ans[-1]>0:#目前有存，且最右邊正的、向右，會相撞
                    if abs(ans[-1]) == abs(a):#絕對值大小都相同，都消滅
                        ans.pop()#吐掉
                        a = 0
                        break#離開迴圈
                    elif abs(ans[-1]) > abs(a):
                        a = 0
                        break
                    else: #左邊比較小，消滅左邊
                        ans.pop()
                if a !=0:ans.append(a)
        return ans
