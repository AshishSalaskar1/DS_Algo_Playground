https://leetcode.com/problems/linked-list-cycle-ii/submissions/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        if(head == null || head.next == null || head.next.next == null )
            return null;
        
        ListNode slow = head.next;
        ListNode fast = head.next.next;
        
        while(fast != slow){
            if(fast == null || fast.next == null) return null;
            
            slow = slow.next;
            fast = fast.next.next;
            
        }
        
        
        fast = head;
        
        while(fast != slow){

            slow = slow.next;
            fast = fast.next;
        }
        
        return slow;
        
    }
}

//Use hashmap for easier approach
/**

1 ) Add each node to hashmap
2 ) If node appears twice return that node 
3 ) If no repeated nodes return false : no cycle found

*/
public class Solution {
    public ListNode detectCycle(ListNode head) {
       Set<ListNode> set = new HashSet<>();
        
       ListNode cur = head;
        
        while(cur != null){
            if(set.contains(cur))
                return cur;
            set.add(cur);
            cur = cur.next;
        }
        
        return null;
    }
}
