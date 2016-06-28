class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    one = ListNode(1)
    two = ListNode(2)
    one.next = two
    print one