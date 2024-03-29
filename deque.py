# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# YOUR NAME

# Hint: pip3 install llist
# from llist import dllist
# Deque Scratchpad
# KRISTEN ORUE
# Use this as a "scratchpad" to tinker with your deque.

from llist import dllist

class Deque:

    def __init__(self):
        self.data = dllist()

    def enqueue_left(self, item):
        self.data.appendleft(item)

    def enqueue_right(self,item):
        self.data.appendright(item)

    def dequeue_left(self):
        return self.data.popleft()

    def dequeue_right(self):
        return self.data.popright()

    def is_empty(self):
       if self.data.first == None:
            return True
