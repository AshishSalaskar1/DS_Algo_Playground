/**

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.


Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        
        if(head == null) 
            return null;
        
        int k = 0;
        ListNode cur = head;
        ListNode prev = null;
        ListNode next = head;
        
        while( cur != null && k<2){
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
            k++;
        }
        
        if(next != null)
            head.next = swapPairs(next);
        
        return prev;
    }
}
