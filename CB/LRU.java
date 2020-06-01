/**


Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

*/

class LRUCache {
    
    //cache element
    static class CE{
        int key,val;
        public CE(int key,int val){
            this.key = key;
            this.val = val;
        }
    }
    
    Deque<CE> q = new LinkedList<>();
    HashMap<Integer,CE> map = new HashMap<>();
    static int maxSize;

    public LRUCache(int capacity) {
        this.maxSize = capacity;
    }
    
    //access operation
    public int get(int key) {
        if(map.containsKey(key)){
            //remove it from queue
            CE removedEle = map.get(key);
            //removal of cacheEle takes O(1)
            q.remove(removedEle);
            // add ele to front as most recently accessed
            q.addFirst(removedEle);
            
            return removedEle.val;
        }
        
        // key not found
        return -1;
    }
    
    public void put(int key, int value) {
        //if key was already there but value may change
        if(map.containsKey(key)){
            CE rEle = map.get(key);
            q.remove(rEle);
        }
        // new entry -> check overflow
        else{
            if(q.size() == maxSize){
                
                CE rEle = q.removeLast();
                // System.out.println("OVERFLOW + removed: " +removeEle.key);
                map.remove(rEle.key);
            }
        }
        
        //Either node is removed if already present
        //Or if !present and size is full ele is remove from back (LRU ele)
        CE ele = new CE(key,value);
        q.addFirst(ele);
        map.put(key,ele);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
