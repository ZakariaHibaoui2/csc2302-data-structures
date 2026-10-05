"""Stack (LIFO) backed by a Python list, plus two classic applications."""


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


def is_balanced(expression):
    """True if every (, [ and { is closed in the right order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()


def eval_postfix(expression):
    """Evaluate a space-separated postfix expression, e.g. '3 4 + 2 *' -> 14."""
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    stack = Stack()
    for token in expression.split():
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.push(ops[token](a, b))
        else:
            stack.push(float(token))
    result = stack.pop()
    if not stack.is_empty():
        raise ValueError("malformed expression")
    return result


if __name__ == "__main__":
    print(is_balanced("{[()()]}"), is_balanced("([)]"))
    print(eval_postfix("3 4 + 2 *"))
