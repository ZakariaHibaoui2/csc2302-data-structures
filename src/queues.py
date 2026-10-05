"""Queue (FIFO) as a fixed-capacity circular array, and a round-robin scheduler."""


class CircularQueue:
    def __init__(self, capacity=8):
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def enqueue(self, item):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        rear = (self._front + self._size) % len(self._data)
        self._data[rear] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._data[self._front]

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _resize(self, capacity):
        old = [self._data[(self._front + i) % len(self._data)] for i in range(self._size)]
        self._data = old + [None] * (capacity - self._size)
        self._front = 0


def round_robin(jobs, quantum):
    """Simulate CPU round-robin scheduling.

    jobs: list of (name, burst_time). Returns the order in which jobs finish.
    """
    queue = CircularQueue()
    for job in jobs:
        queue.enqueue(job)
    finished = []
    while not queue.is_empty():
        name, remaining = queue.dequeue()
        if remaining > quantum:
            queue.enqueue((name, remaining - quantum))
        else:
            finished.append(name)
    return finished


if __name__ == "__main__":
    print(round_robin([("A", 5), ("B", 2), ("C", 7)], quantum=2))
