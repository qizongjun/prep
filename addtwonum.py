# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        c = 0
        l3_head = None
        l3_tail = None

        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            sum = c + x + y
            c = sum / 10

            value = sum % 10

            new_node = ListNode(value)
            if not l3_head:
                l3_head = new_node

            if not l3_tail:
                l3_tail = new_node
            else:
                l3_tail.next = new_node

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next


        return l3_head


if __name__ == '__main__':
    l1 = ListNode(2)
    tail = ListNode(4)
    l1.next = tail
    tail.next = ListNode(3)

    l2 = ListNode(5)
    tail = ListNode(6)
    l2.next = tail
    tail.next = ListNode(4)

    l3 = Solution.addTwoNumbers()