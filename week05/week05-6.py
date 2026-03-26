#week05-6.py 學習計畫 Hash Table
#Leetcode 2352. Equal Row and Column Pairs
#直的橫的完全相同有幾組
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() #Hash map 可以知道有哪些row出現幾次
        for row in grid:
            counter[tuple(row)]+=1

        ans = 0
        for col in zip(*grid):#矩陣transpose 再取出col
            ans += counter[tuple(col)]
        return ans
