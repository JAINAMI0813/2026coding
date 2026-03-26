#week05-4.py 昨天的挑戰題
#Leetcode 3548. Equal Sum Grid Partition II
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row) for row in grid])#全部加起來

        preSum = 0
        for row in grid:
            preSum +=sum(row) #把row 整行加進來
            if preSum == total - preSum:
                return True

        preSum = 0 #對應直切一刀
        for col in zip(*grid):
            preSum += sum(col)
            if preSum == total - preSum:
               return True
        return False
