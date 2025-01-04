"""
Problem: https://leetcode.com/problems/design-task-manager/
- You can add (userid, taskid, priority) to a PQ
- You need to return the task with highest priority when query() is called  (break ties using higher task_id)
- Operations allowed: remove_task(task_id) and edit(task_id, new_priority)

SOLUTION:
- Mantain an hmap[task_id] = (uid,tid,priority)
    - The priority here is the latest on (after lot of edits)
    - If task_id is not there in hmap -> it must have been done / removed
    - This acts like TOMBSTNE marker for DELETE and LATEST_MARKER for updates

- add() -> add to both hmap and pq
- edit() -> replace in hmap -> add new entry with updated priority in hmap
- remove() -> remove from hmap 

QUERY (execTop)
-> Keep on popping the top-most element (highest priority) 
1. if top_most element not present in hmap -> continue (ALREADY DELETED)
2. if priority[top_most_task_id] != priority in hashmap -> continue (THE PRIORITY WAS UPDATED)
-> Continue till (1) and (2) neither is True => VALID ACTUAL TOPMOST


"""
from queue import PriorityQueue
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.hmap = {}
        self.pq = PriorityQueue()

        for [userid, taskid, pr] in tasks:
            self.add(userid, taskid, pr)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        self.hmap[task_id] = (user_id, task_id, priority )
        self.pq.put( (-priority, -task_id, user_id) )

    def edit(self, task_id: int, newPriority: int) -> None:
        user_id, tid, prior = self.hmap[task_id]
        self.hmap[task_id] = (user_id, task_id, newPriority )
        self.pq.put( (-newPriority, -task_id, user_id) )
        
    def rmv(self, task_id: int) -> None:
        self.hmap.pop(task_id)
        
    def execTop(self) -> int:
        while self.pq.qsize() > 0:
            priority, taskid, userid = self.pq.get()
            priority, taskid = -priority, -taskid

            if taskid not in self.hmap:
                continue

            updated_priority = self.hmap[taskid][2]
            if updated_priority != priority:
                continue
            else:
                self.hmap.pop(taskid)
                return userid
            
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()