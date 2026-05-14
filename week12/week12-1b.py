#week12-1b.py 學習計畫 Graph-DFS第一題
#DFS:Depth First Search 通常會利用stack 或function stack
#房間裡有鑰匙，可以再開新的房間
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()#有去過的房間，不要再進去了
        def helper(now):
            for k in rooms[now]:#函式呼叫函式的版本，也能進行DFS
                if k not in visited:
                    visited.add(k)
                    helper(k)
        visited.add(0)
        helper(0)
        return len(rooms) == len(visited)
