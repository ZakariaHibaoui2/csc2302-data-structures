"""Singly linked list with the operations covered in class."""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, values=()):
        self.head = None
        self._size = 0
        for v in values:
            self.append(v)

    def prepend(self, value):
        self.head = ListNode(value, self.head)
        self._size += 1

    def append(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self._size += 1

    def remove(self, value):
        prev, curr = None, self.head
        while curr:
            if curr.value == value:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                self._size -= 1
                return
            prev, curr = curr, curr.next
        raise ValueError(f"{value!r} not in list")

    def find(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        self.head = prev

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return " -> ".join(map(str, self)) or "(empty)"


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3, 4])
    ll.reverse()
    print(ll)
