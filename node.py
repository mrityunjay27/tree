from collections import deque, defaultdict


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
        """
        This traversal is similar to level-order traversal.
        but we need to reverse the array of a level if level is odd.
        :param root:
        :return:
        """
        queue = deque([root] if root else [])
        res = []
        while queue:
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
            current_level = reversed(current_level) if len(res) % 2 else current_level
            res.append(current_level)

        return res

    def boundary_traversal(self, root):
        """
        Traverse boundary to BT

        1. LEFT BOUNDARY WITHOUT LEAF.
        2. LEAVES
        3. RIGHT BOUNDARY WITHOUT LEAF IN REVERSE ORDER
        :param root:
        :return:
        """

        def is_leaf_node(n):
            return n.left and n.right

        def left_boundary_traversal(res ,root):
            """
            WILL BE CALLED BY ROOT OF THE TREE
            Returns left boundary of the BT except the leaf.
            :param res:
            :param root:
            :return:
            """
            current_node = root.left
            while current_node:
                if not is_leaf_node(current_node):
                    res.append(current_node.value)

                current_node = current_node.left if current_node.left else current_node.right

        def right_boundary_traversal(res ,root):
            """
            WILL BE CALLED BY ROOT OF THE TREE
            Returns right boundary of the BT except the leaf in reverse order.
            :param res:
            :param root:
            :return:
            """
            temp = []
            current_node = root.right
            while current_node:
                if not is_leaf_node(current_node):
                    temp.append(current_node.value)

                current_node = current_node.right if current_node.right else current_node.left

            res.extend(reversed(temp))

        def leaf_traversal(res, root):
            """
            Returns the leaf traversal of tree
            :param res:
            :param root:
            :return:
            """
            if is_leaf_node(root):
                res.append(root.value)
                return

            if root.left:
                leaf_traversal(res, root.left)
            if root.right:
                leaf_traversal(res, root.right)



        res = []
        if not is_leaf_node(root):
            res.append(root.value)

        left_boundary_traversal(res, root)
        leaf_traversal(res, root)
        right_boundary_traversal(res, root)

        return res

    def vertical_order_traversal(self, root):
        """
        Things going to HEAT UP.
        Some concept and DS but it is easy.

        For every node we will mark its coordinates.
        Root being at (0,0), X Y (Lets consider down as +)
        Its left (-1,1)
        Its right(1,1)
        ..... and so on.
        :param root:
        :return:
        """

        # and return a 2D list of node values

        # Map to store nodes based on vertical and level information
        nodes = defaultdict(lambda: defaultdict(lambda: set()))
        """
         # why set not list ? because
        to handle cases where multiple nodes could have the same vertical (x) and level (y) values, 
        ensuring that each node value appears only once at that position.
        """

        # Will be like { x_coordinate_1: { y_coordinate_1 : (data1, data2) , y_coordinate_2 : (node.data, )}
        #                x_coordinate_2: { y_coordinate_1 : (data3, data4) , y_coordinate_2 : (node.data5, )}

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical and level information
        todo = deque([(root, (0, 0))])

        # BFS traversal
        while todo:
            # Retrieve the node and its vertical and level information from the front of the queue
            # REMOVE
            temp, (x, y) = todo.popleft()

            # Insert the node value into the corresponding vertical and level in the map
            # PRINT
            nodes[x][y].add(temp.value)

            # ADD
            # Process left child
            if temp.left:
                todo.append((temp.left, (x - 1, y + 1)))

            # Process right child
            if temp.right:
                todo.append((temp.right, (x + 1, y + 1)))

        # Prepare the final result list by combining values from the map
        ans = []
        for x, y_vals in nodes.items():  # x = -1, y_vals = { 1 : (20, 10, 30) }
            col = []
            for y, values in y_vals.items():
                # Insert node values
                # into the column list
                col.extend(sorted(values))
            # Add the column list
            # to the final result
            ans.append(col)

        return ans

    def top_view_of_BT(self, root)-> list :
        """
        Given the root of the tree return the top view of the tree
        first node of each vertical
        :param root:
        :return:
        """

        ans = []

        if not root:
            return ans

        # Map to store the top view nodes based on their vertical positions
        mpp = {}

        # Queue for BFS traversal, each element is a pair containing node and its vertical position
        q = deque([(root, 0)])

        while q:
            # Retrieve the node and its vertical position from the front of the queue
            node, line = q.popleft()

            # If the vertical position is not already in the map, add the node's data to the map
            # Intuition is that if tha line is not in map then for that line we are going to write data for the first time.
            # which eventually means that it is topmost value in that line as we are doing level order traversal.
            if line not in mpp:
                mpp[line] = node.value

            # Process left child
            if node.left:
                q.append((node.left, line - 1))

            # Process right child
            if node.right:
                q.append((node.right, line + 1))

        # Transfer values from the
        # map to the result vector
        for value in sorted(mpp.items()):
            ans.append(value[1])

        return ans

    def bottom_view_of_BT(self, root)-> list :
        """
        Given the root of the tree return the BOTTOM view of the
        :param root:
        # last node if each vertical
        :return:
        """

        ans = []

        if not root:
            return ans

        # Map to store the top view nodes based on their vertical positions
        mpp = {}

        # Queue for BFS traversal, each element is a pair containing node and its vertical position
        q = deque([(root, 0)])

        while q:
            # Retrieve the node and its vertical position from the front of the queue
            node, line = q.popleft()

            # Directly write the node value against its vertical line
            # Intuition: As its level order BFS. Node at the last of any vertical will be processed at the end.
            # and Last node will get over-write any nodes on the same vertical above it.

            mpp[line] = node.value


            # Process left child
            if node.left:
                q.append((node.left, line - 1))

            # Process right child
            if node.right:
                q.append((node.right, line + 1))

        # Transfer values from the
        # map to the result vector
        for value in sorted(mpp.items()):
            ans.append(value[1])

        return ans

    def left_right_view_of_BT(self, root):

        def rightsideView(self, root):
            # Vector to store the result
            res = []

            # Call the recursive function
            # to populate the right-side view
            self.recursionRight(root, 0, res)

            return res

        def leftsideView(self, root):
            # Vector to store the result
            res = []

            # Call the recursive function
            # to populate the left-side view
            self.recursionLeft(root, 0, res)

            return res

        # Recursive function to traverse the
        # binary tree and populate the left-side view
        def recursionLeft(self, root, level, res):
            # Check if the current node is None
            if not root:
                return

            # Check if the size of the result list
            # is equal to the current level
            if len(res) == level:
                # If equal, means so far we have not got any node of this level.
                # add the value of the current node to the result list  (root being at 0)
                res.append(root.data)

            # Recursively call the function for the
            # left child with an increased level
            self.recursionLeft(root.left, level + 1, res)

            # Recursively call the function for the
            # right child with an increased level
            self.recursionLeft(root.right, level + 1, res)

        # Recursive function to traverse the
        # binary tree and populate the right-side view
        def recursionRight(self, root, level, res):
            # Check if the current node is None
            if not root:
                return

            # Check if the size of the result list
            # is equal to the current level
            if len(res) == level:
                # If equal, means so far we have not got any node of this level.
                # add the value of the current node to the result list
                res.append(root.data)

                # Recursively call the function for the
                # right child with an increased level
                self.recursionRight(root.right, level + 1, res)

                # Recursively call the function for the
                # left child with an increased level
                self.recursionRight(root.left, level + 1, res)






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


# print(node.boundary_traversal(node))

print(node.bottom_view_of_BT(node))

