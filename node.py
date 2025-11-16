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
            for i in range(len(queue)):  # This will not change on the fly when we change the content of the q inside loop
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
        level = 0
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
            if level % 2 == 1:
                current_level.reverse()
            res.append(current_level)
            level += 1

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
            return not (n.left and n.right)

        def left_boundary_traversal(res ,root):
            """
            WILL BE CALLED BY ROOT OF THE TREE
            Returns left boundary of the BT except the leaf.
            ITERATIVE APPROACH
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
        Left will be row + 1, col - 1
        Right will be row + 1, col + 1
        :param root:
        :return:
        """

        # and return a 2D list of node values

        # Map to store nodes based on vertical and level information
        nodes = defaultdict(lambda: defaultdict(lambda: list()))

        # Will be like { col_coordinate_1: { row_coordinate_1 : (data1, data2) , row_coordinate_2 : (node.data, )}
        #                col_coordinate_2: { row_coordinate_1 : (data3, data4) , row_coordinate_2 : (node.data5, )}

        # Queue for BFS traversal, each
        # element is a pair containing node
        # and its vertical and level information
        todo = deque([(root, (0, 0))])

        # BFS traversal
        while todo:
            # Retrieve the node and its vertical and level information from the front of the queue
            # REMOVE
            temp, (r, c) = todo.popleft()

            # Insert the node value into the corresponding vertical and level in the map
            # PRINT
            nodes[c][r].append(temp.value)

            # ADD
            # Process left child
            if temp.left:
                todo.append((temp.left, (r + 1, c - 1)))

            # Process right child
            if temp.right:
                todo.append((temp.right, (r + 1, c + 1)))

        # Prepare the final result list by combining values from the map
        ans = []
        for col in sorted(nodes.keys()):
            col_nodes = []
            for row in sorted(nodes[col].keys()):
                col_nodes.extend(sorted(nodes[col][row]))
            ans.append(col_nodes)

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

    def is_symmetric_binary_tree(self, root) -> bool:
        """
        tells whether tree forms a mirror around its root.
        :param root:
        :return:
        """
        def helper(left, right) -> bool:
            """
            Traverse Root Left Right in Left Subtree
            Traverse Root Right Left in Right Subtree
            Do both of them simultaneously.
            :param left:
            :param right:
            :return:
            """
            if not left or not right:  # if any of them is null
                return left == right   # see if both are null. (Base case)

            if left.value != right.value:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)


        return helper(root.left, root.right)

    def root_to_node_path(self, root, target) -> list:
        """
        Back-tracking
        Given a target find its path from root.
        """

        def get_path(ans, node, target):
            """
            Recursive backtracking function

            :param ans:
            :param node:
            :param target:
            :return:
            """
            if not node:
                return False

            ans.append(node.value)

            if node.value == target:  # End the search.
                return True

            # Did not find target yet?
            # See left and right.
            if get_path(ans, node.left, target) or get_path(ans, node.right, target):
                # Target is present in either of the subtree
                return True

            else: # Not present in either side.
                ans.pop()  # FALLBACK !!!
                return False


        ans = []
        if not root:
            return ans
        get_path(ans, root, target)

        return ans

    def lowest_common_ancestor(self, root, a, b):
        """
        Given two node value a and b.
        Find the lowest common ancestor of them

        :param root:
        :param a:
        :param b:
        :return:
        """

        # Recursive DFS solution.
        # Approach is like we will traverse left -> right

        # Base case
        # Reached leaf node or got any of the value, return it.
        # No need to traverse further as we have got what we were looking for.
        if not root or root == a or root == b:
            return root

        # Traverse Left
        answer_from_left_subtree = self.lowest_common_ancestor(root.left, a, b)
        # Traverse Right
        answer_from_right_subtree = self.lowest_common_ancestor(root.right, a, b)

        #  Decide at this node.
        # We got null from left side means target not found in left subtree, return answer from right side
        if not answer_from_left_subtree:
            return answer_from_right_subtree
        # We got null from right side means target not found in right subtree, return answer from left side
        elif not answer_from_right_subtree:
            return answer_from_left_subtree
        # Both side gave us an answer that means this is our answer
        else:
            return root


    def maximum_width_of_BT(self, root):
        """
        Return the maximum width of the BT.
        :param root:
        :return:
        """

        # Width - is the number of nodes between(possibly) any two nodes (both node should exist)
        # Maximum width will be max width among all the levels of BT. It need not be the width of last level.

        # BFS Traversal as we have to do a level order traversal of the Tree.
        # We will index all the nodes in the tree and calculate (right - left + 1) at each level
        # and compare it wil the result variable.

        # But there is catch you cannot start indexing the nodes from 0 or 1 and keep on indexing till number of nodes.
        # Because, for any node with index i its left child will have index (2*i + 1) and right child will have index
        # (2*i + 2). So the indexing number will keep on increasing and will result in overflow.

        # So, to overcome this.
        # For a particular level we will start indexing from beginning only.
        # From the above level, take the minimum index.
        # Do minimum_index - 1
        # And this will be starting index of the current leve.

        # If the root is null, the width is zero
        if not root:
            return 0

        # Initialize a variable 'ans' to store the maximum width
        ans = 0

        # Create a deque to perform level-order traversal,
        # where each element is a tuple of Node and its position in the level
        q = deque()
        # Push the root node and its position (0) into the deque
        q.append((root, 0))

        # Perform level-order traversal
        while q:
            # Get the number of nodes at the current level
            size = len(q)
            # Get the position of the front node in the current level
            mmin = q[0][1]

            # Store the first and last positions of nodes in the current level
            first, last = None, None

            # Process each node in the current level
            for i in range(size):
                # Pop the front of the deque
                node, cur_idx = q.popleft()
                # Calculate current position relative to the minimum position in the level
                cur_idx -= mmin

                # If this is the first node in the level, update the 'first' variable
                if i == 0:
                    first = cur_idx

                # If this is the last node in the level, update the 'last' variable
                if i == size - 1:
                    last = cur_idx

                # Enqueue the left child of the current node with its position
                if node.left:
                    q.append((node.left, cur_idx * 2 + 1))

                # Enqueue the right child of the current node with its position
                if node.right:
                    q.append((node.right, cur_idx * 2 + 2))

            # Update the maximum width by calculating the difference between the first and last positions, and adding 1
            ans = max(ans, last - first + 1)

        # Return the maximum width of the binary tree
        return ans



    def nodes_at_a_distance_K(self, root, target, k):
        """
        Given the root of a binary tree, the value of a target node target, and an integer k,
        return an array of the values of all nodes that have a distance k from the target node.
        :param root:
        :param target:
        :param k:
        :return:
        """

        # We need to mark parents of all the nodes to traverse upwards in the tree.

        def get_parents_map(root):
            """
            Modified level order traversal to return parents map
            :param root:
            :return:
            """
            queue = deque()
            queue.append(root)
            parents_map = {root: None, }
            while len(queue):
                for i in range(len(queue)):
                    # Remove from the queue ( Element that entered first)
                    e = queue.popleft()
                    # Add children to the queue
                    if e.left:
                        queue.append(e.left)
                        parents_map[e.left] = e  # Mark parent
                    if e.right:
                        queue.append(e.right)
                        parents_map[e.right] = e  # Mark parent

            return parents_map

        parents_map = get_parents_map(root)


        # Now we have our parents map ready.
        # From the target node we possibly go in three directions. (Up towards parent, left, right)

        # We will move 1 step in every direction in one shot.
        # When step count will be k, we will stop and return whatever is in queue ds
        # Why at this point queue will be answer?
        # 1. As this is BFS (1 step in every direction), and we would have popped all other nodes while doing BFS process.
        # Also, we have to maintain a data structure for visited nodes

        visited = {}
        q = deque()
        current_level = 0

        q.append(target)
        visited[target] = True

        while q:
            size = len(q)
            if current_level == k:
                break
            current_level += 1
            for i in range(size):
                node = q.popleft()

                # See left
                if node.left and not visited.get(node.left, None):
                    q.append(node.left)
                    visited[node.left] = True

                # See right
                if node.right and not visited.get(node.right, None):
                    q.append(node.right)
                    visited[node.right] = True

                # See up
                if parents_map[node] and visited.get(parents_map[node], None):
                    q.append(parents_map[node])
                    visited[parents_map[node]] = True


        for e in q:
            print(e.value)











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

node.nodes_at_a_distance_K(node, 50,1)

