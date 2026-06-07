# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Map: node value -> TreeNode object
        node_map = {}
        # Set: all nodes that are children (have a parent)
        children = set()
        
        # Process each description
        for parent_val, child_val, is_left in descriptions:
            # Add child to the set
            children.add(child_val)
            
            # Create TreeNode if not exists
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)
            
            # Link parent to child
            parent_node = node_map[parent_val]
            child_node = node_map[child_val]
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        
        # Find root: node that is not in children set (no parent)
        all_nodes = set(node_map.keys())
        root_val = all_nodes - children
        root_val = root_val.pop()  # Get the single root value
        
        return node_map[root_val]
