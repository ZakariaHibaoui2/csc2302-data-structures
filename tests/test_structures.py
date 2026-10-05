import os
import random
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from bst import BST  # noqa: E402
from linked_list import LinkedList  # noqa: E402
from queues import CircularQueue, round_robin  # noqa: E402
from stack import Stack, eval_postfix, is_balanced  # noqa: E402


# ---------- BST ----------
def build(values):
    t = BST()
    for v in values:
        t.append(v)
    return t


def test_bst_inorder_is_sorted():
    values = random.Random(1).sample(range(1000), 200)
    assert build(values).to_list() == sorted(values)


def test_bst_search_recursive_and_iterative():
    t = build([15, 101, 11, 5, 23, 42, 58])
    for v in (15, 5, 58):
        assert t.search(v) and t.search_iter(v)
    assert not t.search(7) and not t.search_iter(7)


@pytest.mark.parametrize("target", [5, 11, 15, 101, 23])
def test_bst_remove_leaf_one_child_two_children(target):
    values = [15, 101, 11, 5, 23, 42, 58]
    t = build(values)
    t.remove(target)
    expected = sorted(values)
    expected.remove(target)
    assert t.to_list() == expected


def test_bst_remove_missing_raises():
    with pytest.raises(ValueError):
        build([1, 2]).remove(3)


def test_bst_random_removals_keep_order():
    rng = random.Random(7)
    values = rng.sample(range(500), 100)
    t = build(values)
    for v in rng.sample(values, 60):
        t.remove(v)
        values.remove(v)
        assert t.to_list() == sorted(values)


# ---------- Stack ----------
def test_stack_lifo():
    s = Stack()
    for i in range(3):
        s.push(i)
    assert [s.pop(), s.pop(), s.pop()] == [2, 1, 0]
    with pytest.raises(IndexError):
        s.pop()


@pytest.mark.parametrize("expr,ok", [("{[()()]}", True), ("([)]", False), ("((", False), ("", True)])
def test_is_balanced(expr, ok):
    assert is_balanced(expr) is ok


def test_eval_postfix():
    assert eval_postfix("3 4 + 2 *") == 14
    assert eval_postfix("5 1 2 + 4 * + 3 -") == 14


# ---------- Queue ----------
def test_circular_queue_fifo_and_resize():
    q = CircularQueue(capacity=2)
    for i in range(10):
        q.enqueue(i)
    assert [q.dequeue() for _ in range(10)] == list(range(10))
    assert q.is_empty()


def test_round_robin_order():
    assert round_robin([("A", 5), ("B", 2), ("C", 7)], quantum=2) == ["B", "A", "C"]


# ---------- Linked list ----------
def test_linked_list_ops():
    ll = LinkedList([1, 2, 3])
    ll.prepend(0)
    ll.remove(2)
    assert list(ll) == [0, 1, 3] and len(ll) == 3
    ll.reverse()
    assert list(ll) == [3, 1, 0]
    assert ll.find(1) and not ll.find(2)
