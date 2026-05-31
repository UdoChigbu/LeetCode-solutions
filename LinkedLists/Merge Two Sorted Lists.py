class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
   def build_list(self, arr):
    dummy = ListNode()
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next
   
   
   def mergeTwoLists(self, list1, list2):
    if not list1:
        return list2
    if not list2:
         return list1  
      #if list 1 value is< list 2 value
    if list1.val < list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    #if list2 value< list1 value
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
       



    
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
    
solution = Solution()
l1 = solution.build_list([1,2,4])
l2 = solution.build_list([1,3,4])

result = solution.mergeTwoLists(l1, l2)

print_list(result)