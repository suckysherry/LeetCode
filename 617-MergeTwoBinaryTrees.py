def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        tree = None
        if t1 == None and t2 != None:
            return t2
        elif t1 != None and t2 == None:
            return t1
        elif t1 == t2 == None:
            return None
        else:
            tree = TreeNode(t1.val + t2.val)
            tree.left = self.mergeTrees(t1.left, t2.left)
            tree.right = self.mergeTrees(t1.right, t2.right)
        return tree