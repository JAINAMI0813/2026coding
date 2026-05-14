#week12-4.py 學習計畫 Graph - DFS
#Leetcode 1466. Reorder Routes to Make All Paths Lead to the City Zero
#解法:從0出發，全部走過，路不對，就ans +=1
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set() #走過的 不要再走
        ans = 0
        path = defaultdict(list)#path[now]與哪些程式相接
        for a,b in connections:
            path[a].append((b,+1))
            path[b].append((a,-1))

        def helper(now):
            ans = 0
            visited.add(now)
            for k,d in path[now]:#城市now 可以到城市k,方向是d
                if k not in visited:
                    if d==+1:ans +=1 #要檢測方向，若方向「出錯」+1]
                    ans += helper(k)
            return ans
        return helper(0)
