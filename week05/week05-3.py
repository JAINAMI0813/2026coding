#week05-3.py 厩策璸礶糶程篊セ
#Leetcode 1207. Unique Number of Occurrences
#–贺计 瞷Ω计常ぃ妓
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter =  Counter(arr)#参璸计瞷Ω计
        s = set()
        for c in counter:
            if counter[c] in s:
                return False
            s.add(counter[c])
        return True
