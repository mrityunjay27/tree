from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def printNode(self):
        print(self.value)

    def insert_node(self, value):
        """
        Assuming it to be BST.
        Will be called by Root of the tree
        :param value:
        :return:
        """
        if self.value and value > self.value:
            # Greater than parent. Add to the right.
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert_node(value)

        elif self.value and value <= self.value:
            # Less than the parent. Add to the left.
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert_node(value)

        else:
            self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()


    def inorder_traversal(self, root):
        """

        #DFS
        given the root of the tree.
        give inorder traversal.
        LEFT VALUE RIGHT
        :param root:
        :return:
        """
        res = []
        if root:
            res = self.inorder_traversal(root.left)  # GO LEFT
            res.append(root.value) # CURRENT
            res = res + self.inorder_traversal(root.right)  # GO RIGHT

        return res


    def level_order_traversal(self, root):
        """
        Given the root of a tree
        Return level-order traversal of the tree
        works on RPA (Remove , Print, Add Child)
        :param root:
        :return:
        """
        queue = deque()
        queue.append(root)
        res = []
        while len(queue):
            current_level = []
            for i in range(len(queue)):
                # Remove from the queue ( Element that entered first)
                e = queue.popleft()
                # Add to current level
                current_level.append(e.value)
                # Add children to the queue
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            res.append(current_level)

        return res


    def height_of_tree(self,root) -> int:
        if not root:
            # Touched a leaf
            return 0
        height_from_left_subtree = self.height_of_tree(root.left)
        height_from_right_subtree = self.height_of_tree(root.right)

        return max(height_from_left_subtree, height_from_right_subtree) + 1


    def mirror_of_a_BT(self, root):
        """
        Given a root return its mirror.
        :param root:
        :return:
        """
        if not root:
            return None

        mirrored_left_subtree = self.mirror_of_a_BT(root.left)
        mirrored_right_subtree = self.mirror_of_a_BT(root.right)

        root.right = mirrored_left_subtree
        root.left = mirrored_right_subtree

        return root

    def zigzag_traversal(self, root):
        pass

node = Node(10)
node.insert_node(30)
node.insert_node(9)
node.insert_node(1)
node.insert_node(4)
node.insert_node(43)
node.insert_node(34)
node.insert_node(50)

# node.PrintTree()

# print(node.inorder_traversal(node))

# print(node.level_order_traversal(node))
# mirror = node.mirror_of_a_BT(node)
# print(mirror.level_order_traversal(mirror))


