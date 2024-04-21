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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode res = head;
        int carry = 0;
        int sum = 0;
        int v1 = 0,v2=0;
        
        while(l1 != null || l2 != null){
            v1 = (l1 == null) ? 0 : l1.val;
            v2 = (l2 == null) ? 0 : l2.val;
            
            sum = carry + v1 + v2;

            carry = sum / 10;
            
            res.next = new ListNode(sum % 10);
            
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
            res = res.next;
        }
        
        if(carry != 0)
            res.next = new ListNode(carry);
        
        return head.next;
    }
}
