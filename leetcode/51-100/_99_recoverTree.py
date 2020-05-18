# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None

class Solution(object):
     def recoverTree(self, root):
          """
          :type root: TreeNode
          :rtype: None Do not return anything, modify root in-place instead.
          """
          big_node = None
          small_node = None

          pre_node = None # 中序遍历的前一个节点
          # 进行莫里斯中序遍历, big_node一定出现在第一个至倒数第二个节点处，small_node一定第二个到倒数第一个节点处

          p = root
          while p:
               if p.left:
                    # 找到前驱节点
                    precursor = p.left
                    while precursor.right and precursor.right != p:
                         precursor = precursor.right

                    # 前驱节点的右孩子是空节点，则指向p，方便遍历完p的左子树后，返回p位置
                    if precursor.right == None:
                         precursor.right = p
                         p = p.left

                    # 前驱节点的右孩子为p，说明已经遍历完p的左子树
                    else: # precursion.right == p
                         if not big_node and pre_node and pre_node.val > p.val:
                              big_node = pre_node
                         if big_node and pre_node and p.val > big_node.val and pre_node.val < big_node.val:
                              small_node = pre_node

                         precursor.right = None
                         pre_node = p
                         p = p.right
               else:
                    if not big_node and pre_node and pre_node.val > p.val:
                         big_node = pre_node
                    if big_node and pre_node and p.val > big_node.val and pre_node.val < big_node.val:
                         small_node = pre_node
                    pre_node = p
                    p = p.right

          if not small_node:
               # small_node是最后一个元素
               small_node = pre_node

          big_node.val, small_node.val = small_node.val, big_node.val




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)

    Solution().recoverTree(root)
    print(root.val)
    print(root.left.val)
    print(root.left.right.val)

