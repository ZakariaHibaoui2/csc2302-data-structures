"""Binary Search Tree - recursive and iterative operations."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if value <= root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self.insert(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
            else:
                self.insert(root.right, value)

    def append(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert(self.root, value)

    def search(self, target):
        def _search(root, target):
            if root is None:
                return False
            if root.value == target:
                return True
            elif target < root.value:
                return _search(root.left, target)
            else:
                return _search(root.right, target)
        return _search(self.root, target)

    def search_iter(self, target):
        curr = self.root
        while curr:
            if curr.value == target:
                return True
            elif target < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def remove(self, target):
        p_curr, curr = None, self.root
        while curr:
            if curr.value == target:
                break
            elif target < curr.value:
                p_curr, curr = curr, curr.left
            else:
                p_curr, curr = curr, curr.right
        if curr is None:
            raise ValueError("Target Not found!!")

        if curr.left and curr.right:
            # Two children: copy the in-order successor, then unlink it.
            p_succ, succ = curr, curr.right
            while succ.left:
                p_succ, succ = succ, succ.left
            curr.value = succ.value
            if p_succ.left is succ:
                p_succ.left = succ.right
            else:
                p_succ.right = succ.right
        else:
            child = curr.left or curr.right
            if p_curr is None:
                self.root = child
            elif p_curr.left is curr:
                p_curr.left = child
            else:
                p_curr.right = child

    def to_list(self):
        """In-order values as a list (sorted order)."""
        out = []

        def _walk(root):
            if root is None:
                return
            _walk(root.left)
            out.append(root.value)
            _walk(root.right)
        _walk(self.root)
        return out

    def height(self):
        def _h(root):
            return 0 if root is None else 1 + max(_h(root.left), _h(root.right))
        return _h(self.root)

    def inorder(self):
        print(*self.to_list())

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        print(root.value, end=" ")
        self.traverse(root.right)


if __name__ == "__main__":
    t1 = BST()
    for v in (15, 101, 11, 5, 23, 42, 58):
        t1.append(v)
    t1.inorder()
    t1.remove(5)
    t1.inorder()
    t1.remove(15)          # node with two children
    t1.inorder()
