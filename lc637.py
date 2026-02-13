# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levelNodes = [root]
        avg = []
        while(levelNodes!=[]):
            n = 0
            acc = 0
            copyArr = [] 
            for node in levelNodes:
                n+=1
                acc+=node.val
            avg.append(acc/n)
            copyArr = levelNodes.copy()
            for node in copyArr:
                levelNodes.pop(0)    
                if node.left:
                    levelNodes.append(node.left)
                if node.right:
                    levelNodes.append(node.right)
        return avg

