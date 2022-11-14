""" Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children. """



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        results = []

        def traverse(root, s):
            if not root.left and not root.right:
                s = s + str(root.val)
                results.append(s)

            s = s + str(root.val) + "->"
            print(s)

            if root.left:
                left = traverse(root.left, s)
            
            if root.right:
                right = traverse(root.right, s)

        traverse(root, "")
        return results
    
    
    
    #     results = []
    #     if root == None:
    #         return results

    #     current_path = root.val
    #     if root.left == None and root.right == None:
    #         result.append(current_path)
    #     if root.left != None:
    #         traverse(root.left, current_path, result)
    #     if root.right != None:
    #         traverse(root.right, current_path, result)
    #     return result

    # def traverse(node, current_node, result):
    #     current_path += "->" + node.val

    #     results.append(current_node.val)

    #     if node.left == None and node.right == None:
    #         result.append(current_path)
    #         return 

    #     if node.left != None:
    #         traverse(node.left, current_path, result)
    #     if node.right != None:
    #         traverse(node.right, current_path, result)
        


