# 237. Delete Node in a Linked List
#
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
# the linked list should become 1 -> 2 -> 4 after calling your function.
#

# http://www.tangjikai.com/algorithms/leetcode-237-delete-node-in-a-linked-list
# replace current node's value with next node's.
# cur.next = cur.next.next in order to skip the next node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        We can't really delete the node,
        but we can kinda achieve the same effect by instead removing the next node
        after copying its data into the node that we were asked to delete.
        """
        node.val = node.next.val
        node.next = node.next.next

