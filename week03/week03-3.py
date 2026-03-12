#week03-3.py 學習計畫 sliding window 第二題
#Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') #把五個字母 變成set()
        #以後用 if c in vowels: 就可以快速確認他是母音
        #以前 if c=='a' or c =='e' or c=='o' or c=='u':
        count = 0
        for i in range(k):
            if s[i] in vowels: count +=1
        ans = count
        N = len(s)#全部字串的長度 N
        for i in range(k,N):
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -=1
            ans = max(ans, count)
        return ans
