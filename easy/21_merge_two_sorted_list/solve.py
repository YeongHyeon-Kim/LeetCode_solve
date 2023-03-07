from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = []
list2 = []


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    next_ = result
    while list1 != None and list2 != None:
        if list1.val <= list2.val:
            next_.next = list1
            list1 = list1.next
        else:
            next_.next = list2
            list2 = list2.next
        next_ = next_.next

    if list1 != None:
        next_.next = list1
    else:
        next_.next = list2
    return result.next


# result = ListNode()
# next_ = result
# while True:
#     if list1 == None and list2 == None:
#         return result
#     elif list1 == None:
#         while list2 != None:
#             tmp_node = ListNode(list2.val)
#             next_ = tmp_node
#             next_ = next_.next
#             list2 = list2.next
#         return result
#     elif list2 == None:
#         while list1 != None:
#             tmp_node = ListNode(list2.val)
#             next_ = tmp_node
#             next_ = next_.next
#             list1 = list1.next
#         return result

#     if list1.val <= list2.val:
#         tmp_node = ListNode(list1.val)
#         list1 = list1.next
#     else:
#         tmp_node = ListNode(list2.val)
#         list2 = list2.next
#     next_ = tmp_node
#     next_ = next_.next

mergeTwoLists(list1, list2)
