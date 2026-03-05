#week02-3.py 學習計畫 Two Pointers 第二題
#LeetCode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1,N2 = len(s), len(t)
        if N1==0: return True

        i = 0 #i 從0開始
        for k in range(N2):#右邊一個個去試
            if s[i] == t[k]:
                i += 1
            if i==N1:
                return True

        #沒有走到最後 沒有比對成功
        return False
