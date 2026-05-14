#week12-3.py 學習計畫 Graph - DFS
#LeetCode 547. Number of Provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)#先知道有幾個Nodes
        visited = set()

        def helper(now):
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)
        ans = 0 #有幾群是相連的
        for i in range(N):#全部node檢查一次
            if i not in visited:
                ans +=1 #代表是新的一群
                helper(i)#函式呼叫函式，暴力把鄰居的鄰居全部走過
        return ans
