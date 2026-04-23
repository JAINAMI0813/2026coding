#week09-5.py 學習計畫 Link List 第一題 把中間的node刪掉
#Leetcode 2095. Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = fast = slow = head #fast兔子

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        #print(slow.val)#當兔子到終點時，烏龜在中間(沒錯)
        prev.next = slow.next
        return head
