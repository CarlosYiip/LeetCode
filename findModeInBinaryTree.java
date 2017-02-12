/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.ArrayList;
public class Solution {
    private int cur_count = 1;
    private int max_count = 1;
    private int pre_val = -1000000;
    private ArrayList<Integer> res = new ArrayList<Integer>();
    
    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
    
        if (pre_val != -1000000) {
            if (node.val == pre_val) {
                cur_count++;
            } else {
                cur_count = 1;
            }
            
            if (cur_count > max_count) {
                max_count = cur_count;
            }
            pre_val = node.val;
            
        } else {
            pre_val = node.val;
        }
        inorder(node.right);
    }
    
    private void fetch(TreeNode node) {
        if (node == null) return;
        
        fetch(node.left);
        
        if (pre_val != -1) {
            if (node.val == pre_val) {
                cur_count++;
            } else {
                if (cur_count == max_count && pre_val != -1000000)
                    res.add(pre_val);
                cur_count = 1;
            }
            pre_val = node.val;
        } else {
            pre_val = node.val;
        }
        
        fetch(node.right);
    }

    public int[] findMode(TreeNode root) {
        pre_val = -1000000;
        inorder(root);
        pre_val = -1000000;
        cur_count = 1;
        fetch(root);
        if (cur_count == max_count && pre_val != -1000000)
            res.add(pre_val);
            
        System.out.println(res);
        
        int[] ress = new int[res.size()];
        
        for (int i = 0; i < res.size(); i++)
            ress[i] = res.get(i);
        
        return ress;
    }
}