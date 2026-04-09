#week07-4.py 厩策璸礶 stack 材肈
#Leetcode 394. Decode String
#盢﹃秆絏计狡Ω计
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        nowN, nowS = 0, ''
        for c in s:
            if c.isdigit():
                nowN = nowN * 10 + int(c)#璝琌计碞秈癘癬ㄓ
            elif c.isalpha():
                nowS += c
            elif c =='[':
                stack.append((nowN, nowS))
                nowN, nowS = 0,''
            elif c ==']':
                prevN, prevS = stack.pop()
                nowS = prevS + prevN * nowS
        return nowS
