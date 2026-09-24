from collections import deque
from dataclasses import dataclass

@dataclass
class TreeNode:
    key: int
    val: int
    children: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

    def push(self, other: TreeNode):
        if self.key == other.key:
            self.val = other.val
            return

        if other.key < self.key:
            if self.left:
                self.left.push(other)
            else:
                self.left = other
        elif self.right is None:
            self.right = other
        else:
            self.right.push(other)
        self.children += 1

class TreeMap:
    
    def __init__(self):
        self._root = None

    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key=key, val=val)
        if self._root is None:
            self._root = node
        else:
            self._root.push(node)

    def _find(self, key: int) -> tuple[TreeNode, TreeNode | None] | None:
        parent = None
        node = self._root
        while node is not None:
            if node.key == key:
                break

            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        return (node, parent)

    def get(self, key: int) -> int:
        node, _parent = self._find(key)
        return -1 if node is None else node.val

    def getMin(self) -> int:
        node = min_node = self._root
        while node is not None:
            if node.key < min_node.key:
                min_node = node
            node = node.left
        return min_node.val if min_node else -1


    def getMax(self) -> int:
        node = max_node = self._root
        while node is not None:
            if node.key > max_node.key:
                max_node = node
            node = node.right
        return max_node.val if max_node else -1

    def remove(self, key: int) -> None:
        node_to_remove, parent = self._find(key)
        if node_to_remove is None:
            return None

        left = node_to_remove.left
        right = node_to_remove.right
        def update_root(n: TreeNode):
            self._root = n
        update_parent = update_root
        if parent:
            parent.children -= 1
            if parent.left is node_to_remove:
                def update_left(n: TreeNode):
                    parent.left = n
                update_parent = update_left
            else:
                def update_right(n: TreeNode):
                    parent.right = n
                update_parent = update_right

        if left is None:
            update_parent(right)
            return
        if right is None:
            update_parent(left)
            return

        if left.children <= right.children:
            root_branch = right
            child_branch = left
        else:
            root_branch = left
            child_branch = right

        root_branch.push(child_branch)
        update_parent(root_branch)
        node_to_remove.left = None
        node_to_remove.right = None

    def _forEach(self, callback: Callable[[TreeNode],bool|None]):
        if not self._root:
            return
        nodes = deque([self._root])
        visited = set([])
        while nodes:
            n = nodes.pop()
            if n.left and n.left.val not in visited:
                nodes.append(n)
                nodes.append(n.left)
                continue
            continue_iteration = callback(n)
            if isinstance(continue_iteration, bool) and not continue_iteration:
                break
            visited.add(n.val)
            if n.right:
                nodes.append(n.right)


    def getInorderKeys(self) -> List[int]:
        if not self._root:
            return []

        result = []
        nodes = deque([self._root])
        visited = set([])
        while nodes:
            n = nodes.pop()
            if n.left and n.left.key not in visited:
                nodes.append(n)
                nodes.append(n.left)
                continue
            result.append(n.key)
            visited.add(n.key)
            if n.right:
                nodes.append(n.right)
        return result
