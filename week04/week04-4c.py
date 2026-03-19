#week04-4c.py (重寫week04-4b.py)
 class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = Counter(nums)#使用進階資料結構 可以統計數量
        for nn in nuns:
            if nn % 2 ==0 and H[nn]==1: return nn
        return -1
#week04-4b.py (重寫week04-3.py)
 class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] *200 #很多很多格，H[??]對應 ??出現幾次
        for nn in nums:
            H[nn] += 1
        #逐個檢查偶數出現幾次
        for nn in nums:#逐一檢查
            if nn % 2 == 0 and H[nn]==1:#偶數才處理
              return nn
        return -1
