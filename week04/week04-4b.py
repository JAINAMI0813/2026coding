#week04-4b.py (糶week04-3.py)
 class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] *200 #H[??]癸莱 ??瞷碭Ω
        for nn in nums:
            H[nn] += 1
        #硋浪琩案计瞷碭Ω
        for nn in nums:#硋浪琩
            if nn % 2 == 0 and H[nn]==1:#案计矪瞶
              return nn
        return -1
