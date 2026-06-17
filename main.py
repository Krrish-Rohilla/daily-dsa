from typing import Self

class FakeListNode:
    def __init__(self, val=None, next: Self = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __add__(self, element: int) -> 'FakeListNode':
        self.next = FakeListNode(element)
        return self.next

    def __radd__(self, element: str):
        self.next = FakeListNode(element)
        return self.next



a = FakeListNode(1)
curr: FakeListNode | None = a
a = "hi" + a + 2 + 3 + 4 + 5 + 6

while curr:
    print(curr)
    curr = curr.next

