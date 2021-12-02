// Problem Link : https://leetcode.com/problems/palindrome-linked-list/
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
    
    static ListNode reverseList(ListNode cur){
        ListNode prev = null,next;
        
        while(cur != null){
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        
        return prev;
    }
    
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        
        //find mid of list
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }

        //reverse second half
        slow = reverseList(slow);
        fast = head;
        System.out.println("NEW MID: "+slow.val);
    
        while(slow != null){
            if(fast.val != slow.val)    
                return false;
            
            slow = slow.next;
            fast = fast.next;
        }
        
        return true;
    }
}
