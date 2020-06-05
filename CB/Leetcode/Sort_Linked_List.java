/**
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

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
    
    static ListNode merge(ListNode a,ListNode b){
        ListNode res = new ListNode(0);
        ListNode resHead = res;
        
        while( a != null && b != null){
            if( a.val < b.val){
                resHead.next = a;
                a = a.next;
            }
            else{
                resHead.next = b;
                b = b.next; 
            }
            
            resHead = resHead.next;
        }
        
        resHead.next = ( a == null) ? b : a;
        
        return res.next;
    }
    
    static ListNode mergeSort(ListNode head){
        if(head == null || head.next == null) 
            return head;
        
        //get one node before mid
        ListNode prev = head;
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast != null && fast.next != null){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        //break the list into halves
        prev.next = null;
        
        ListNode left_head = mergeSort(head);
        ListNode right_head = mergeSort(slow);
        
        return merge(left_head,right_head);
    }

    
    public ListNode sortList(ListNode head) {
        return mergeSort(head);
        
    }
}

