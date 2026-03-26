#week05-5.py 昨天的挑戰題
#Leetcode 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)#統計用過的字母、出現的次數
        counter2 = Counter(word2)
        #用過相同的字母是否是相同的組合(左邊有、右邊也會有)
        if set(counter1.keys())!=set(counter2.keys()):
           return False
        if sorted(counter1.values())!= sorted(counter2.values()):
            return False
        return True
