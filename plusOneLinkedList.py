class Solution(object):
    def plusOne(self, head):
        node = head
        number, n  = node.val, 1
        while node.next:
            node = node.next
            n += 1
            number = number * 10 + node.val
        number += 1
        l = []
        while number:
            l.append(number % 10)
            number /= 10
        l.reverse()
        
        head = ListNode(l[0])
        node = head
        for i in l[1:]:
            node.next = ListNode(i)
            node = node.next
        return head
