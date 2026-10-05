# CSC2302 — Data Structures in Python

> Clean, tested Python implementations of the core data structures from **CSC2302 Data Structures** at Al Akhawayn University, plus a script that generates a complete 40+ page study guide as a PDF.

[![Tests](https://github.com/ZakariaHibaoui2/csc2302-data-structures/actions/workflows/tests.yml/badge.svg)](https://github.com/ZakariaHibaoui2/csc2302-data-structures/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Contents

| Structure | File | Operations | Complexity |
|---|---|---|---|
| **Binary Search Tree** | [`src/bst.py`](src/bst.py) | insert, recursive + iterative search, delete (0/1/2 children via in-order successor), in-order traversal, height | O(h) per op |
| **Stack** | [`src/stack.py`](src/stack.py) | push, pop, peek + **balanced brackets** and **postfix evaluation** | O(1) |
| **Queue** | [`src/queues.py`](src/queues.py) | circular array with auto-resize + **round-robin CPU scheduler** simulation | O(1) amortised |
| **Linked list** | [`src/linked_list.py`](src/linked_list.py) | prepend, append, find, remove, in-place reverse, iteration | O(1) / O(n) |

## Quick start

```bash
git clone https://github.com/ZakariaHibaoui2/csc2302-data-structures.git
cd csc2302-data-structures
pip install -r requirements.txt

python src/bst.py          # demo
pytest -v                  # 18 tests
```

```python
from bst import BST
t = BST()
for v in (15, 101, 11, 5, 23, 42, 58):
    t.append(v)
t.remove(15)              # node with two children
print(t.to_list())        # [5, 11, 23, 42, 58, 101]
```

## Study guide generator

[`tools/generate_guide.py`](tools/generate_guide.py) uses **ReportLab** to build [`docs/CSC2302_Complete_Guide.pdf`](docs/CSC2302_Complete_Guide.pdf), a plain-English guide to the whole course: recursion, stacks and queues (with case studies), trees, BSTs, and practice questions.

```bash
python tools/generate_guide.py
```

## Testing

The tests cover edge cases (empty structures, deleting the root, deleting nodes with two children) and property-style checks: after 60 random deletions, the BST must still produce sorted output. CI runs on Python 3.10 and 3.12.

## Author

**Zakaria Hibaoui** — [GitHub](https://github.com/ZakariaHibaoui2) · [LinkedIn](https://www.linkedin.com/in/zakaria-hibaoui-08b235337/)
Al Akhawayn University in Ifrane, Morocco.

## License

[MIT](LICENSE)
