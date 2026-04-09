#week07-6.py
#Leetcode 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        quene = deque(list(senate))

        banR,banD = 0,0 #目前被消滅的次數都還是0
        R,D = senate.count('R'),senate.count('D') #字串裡，數一數
        while quene:
            now = quene.popleft()
            if now =='R':
                if banR>0:#已經要記錄消滅一個人
                    banR -=1#用掉一個消滅的名額
                    R -=1 #馬上少掉一個人
                else:
                    banD += 1
                    quene.append(now)#再到最右邊排隊
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                else:
                    banR += 1
                    quene.append(now)
            if R==0: return 'Dire'
            if D==0: return 'Radiant'
