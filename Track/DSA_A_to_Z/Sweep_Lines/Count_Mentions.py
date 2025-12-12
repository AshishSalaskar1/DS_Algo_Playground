"""
https://leetcode.com/problems/count-mentions-per-user/submissions/1853489085/?envType=daily-question&envId=2025-12-12

Classic Sweepline -> interesting ordering
1. Give pref to OFFLINE events before MESSAGE -> AOFFLINE, BMESSAGE
2. Within OFFLINE give more pref to offline ending -> AEND, BSTART
    - think of this logically. If at `ts` it comes online n then again goes back offline

APPROACH 1:
- online_set: contains all users online
- If UPDATE_ALL -> mantain global counter since every ele gets updated

APPROACH 2:
- we know that size(online_set) >> size(offline_set)
- Mantain a offline_set
    - when any update happens on HERE (only online)
    - Do mention[offline_usr] -= 1 => all_mention+=1
"""

class Solution:
    def countMentions(self, n: int, event_stream: List[List[str]]) -> List[int]:
        events = []

        for qtype, ts, users in event_stream:
            # OFFLINE/ONLINE events are handled before any MESSAGE on same ts
            if qtype == "OFFLINE":
                events.append((int(ts),"AOFFLINE","BSTART",int(users)))
                events.append((int(ts)+60,"AOFFLINE","AEND",int(users)))
            else:
                events.append((int(ts),"BMESSAGE", "ZZZ", users))

        online, offline = set(list(range(n))),set()
        mentions = [0]*n
        all_notify = 0

        events.sort()

        for ts, qtype, subop, users in events:
            if qtype == "BMESSAGE":
                if users == "HERE": 
                    for online_user in online: mentions[online_user] += 1
                elif users == "ALL": all_notify += 1
                else: # user list
                    user_list = [int(x[2:]) for x in users.split(" ")]
                    for user in user_list: mentions[user] += 1
            elif qtype=="AOFFLINE" and subop=="BSTART": online.discard(users)
            elif qtype=="AOFFLINE" and subop=="AEND": online.add(users)

        for i in range(n): mentions[i] += all_notify
        return mentions

                

            



        
        