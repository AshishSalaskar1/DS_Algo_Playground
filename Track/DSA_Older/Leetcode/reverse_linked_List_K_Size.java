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
        
        ListNode cur = head,prev = null,next=null;
 	
	// k =2 : swap pairs       
        int k = 0;
        while( cur!=null && k<2){
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
