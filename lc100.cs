/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

using System.Collections.Generic;

public class Solution {
    public bool IsSameTree(TreeNode p, TreeNode q) {
        PriorityQueue<TreeNode,int> queueA = new PriorityQueue<TreeNode,int>();
        PriorityQueue<TreeNode,int> queueB = new PriorityQueue<TreeNode,int>();

        int priority = 1;

        queueA.Enqueue(p,priority);
        queueB.Enqueue(q,priority);

        while(queueA.Count > 0 && queueB.Count > 0) {
            TreeNode a = queueA.Dequeue();
            TreeNode b = queueB.Dequeue();
            if (a==null || b==null) {
                if(a==null & b==null) {
                    continue;
                } else {
                    return false;
                }
            }
            if (a.val == b.val) {
                priority++; 
                queueA.Enqueue(a.left, priority);
                queueB.Enqueue(b.left, priority);
                priority++;
                queueA.Enqueue(a.right, priority);
                queueB.Enqueue(b.right, priority);
            } else {
                return false;
            };
        };
        return true;
    }
}
