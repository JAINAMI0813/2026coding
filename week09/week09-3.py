#week09-2.py 學習計畫 Linked List 第三題
#Leetcode 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = [] #容易理解的方法
        while head:
            a.append( head.val)
            head = head.next
        now = ans = ListNode()

        N =len(a)
        for i in range(N-1,-1,-1):
            now.next = ListNode(a[i])
            now = now.next
        return ans.next
