#week09-6.py 學習計畫 Link list 第二題
#Leetcode 328. Odd Even Linked List  偶數堆、奇數堆 串起來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []#先轉成陣列a
        while head:#逐一將Linked List 的值，放入陣列a
            a.append(head.val)
            head = head.next

        N = len(a)
        now = ans =ListNode() #答案，有個Node 右邊會塞真的Nodes
        for i in range(0,N,2):
            now.next = ListNode( a[i] )
            now = now.next #串接下一個
        for i in range(1,N,2):
            now.next = ListNode( a[i] )#逐一塞進去
            now = now.next#串接下一個
        return ans.next
