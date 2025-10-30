"""
PROBLEM:
Accounts: 
   1. ["John","johnsmith@mail.com","john_newyork@mail.com"],
   2. ["John","johnsmith@mail.com","john00@mail.com"],
   3. ["Mary","mary@mail.com"],
   4. ["John","johnnybravo@mail.com"]
- Here names can be same. John in (1) and (4) is different, (1) and (2) is same
- You can merge two accounts IFF they have a email in common. (1) and (2) have johnsmith@mail.com common
- Merge all such possible, after merging sort based on emails


SOLUTION:
- Assign a index(row_number) for each account. This will get combined later
- Mantain a email<->owner dict called `parent_accounts`

FOR acc_id, emails in accounts:
    FOR email in emails:
        - if email not in parent_account => parent_accounts[email] = acc_id
        - else: means this email is already added into some other account
          Merge that and this account => ds.union(acc_id, parent_accounts[email])
          
-> After this you have the UF done, you have list of emails n its parent (unioned ones wont be here)
res = []
-> for email, parent in parent_accounts: # parent = idx (since owner names can be duplicates)
    cur_parent = uf.find_parent(parent) # safety since path compression might not have happened for all
    if cur_parent in res => res[cur_parent] = [email]
    else -> res[cur_parent].append(email)
    

-> Convert your parent_id into names and then sort emails based


💡Tricky Part: Since account names can be duplicates -> how do you differentiate 2 johns?
APPROACH 1
- Assign index to each acc_name and then you just keep on union these acc_indexes
- Maintain dict to check which email belongs to which acc_idx, then if its already seen UNION( current, seen_acc_idx)

APPROACH 2
- Consider unioning <email1, email2>. But store dict<email: acc_name>
- For each union first email with remanining ones. Iterate all emails -> find their parent and add to list 
- Then at last, replace parent email with its acc_name

https://leetcode.com/problems/accounts-merge/submissions/1816252745/"

""" 
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.sizes = [1 for _ in range(n)]

    def find_parent(self, node):        
        if self.parents[node] == node:
            return node
        
        self.parents[node] = self.find_parent(self.parents[node])
        return self.parents[node]

    def union(self, u, v):
        pu,pv = self.find_parent(u), self.find_parent(v)

        if pu == pv:
            return
        elif self.sizes[pu] < self.sizes[pv]:
            self.parents[pu] = pv
            self.sizes[pv] += self.sizes[pu]
        else:
            self.parents[pv] = pu
            self.sizes[pu] += self.sizes[pv]
    
class Solution:
    def combine_accounts(self, acc1_emails, acc2_emails):
        emails = list(set([*acc1_emails, *acc2_emails]))
        return sorted(emails)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        parent_accounts = {}

        res = {}

        for acc_idx, account in enumerate(accounts):
            owner, emails = account[0], account[1:]
            for email in emails:
                if email not in parent_accounts: # first time seen email
                    parent_accounts[email] = acc_idx
                else: # already present -> dont add again BUT union both account_ids
                    dsu.union(acc_idx, parent_accounts[email])
        
        # find unioned parent indexes and join them
        res = {} # acc_id: Set_of_emails
        for email, cur_parent in parent_accounts.items():
            # parents got update after all the unions
            parent_id = dsu.find_parent(cur_parent) # cant use acc_name as key -> duplicated names allowed
            if parent_id not in res:
                res[parent_id] = set([email])
            else:
                res[parent_id].add(email)
        
        # {acc_id:set_of_mails} => [ [acc_name, email1, email2], [acc_name, email1, email2] ]
        
        return [[accounts[acc_id][0],*sorted(list(emails))] for acc_id, emails in res.items()]



from collections import defaultdict
class UF:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def union(self, email1, email2):
        for email in [email1, email2]:
            if email not in self.parent: 
                self.parent[email] = email
                self.size[email] = 1
        
        p1, p2 = self.find_parent(email1), self.find_parent(email2)

        if p1 == p2: return
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map = {}
        uf = UF()
        for account in accounts:
            
            acc_name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_map[email] = acc_name
                uf.union(first_email, email)
        
        res = defaultdict(list)
        for email, acc_name in email_map.items():
            par = uf.find_parent(email)
            res[par].append(email)
        
        final_res = []

        for parent_email, emails in res.items():
            final_res.append(
                [
                    email_map[parent_email],
                    *(sorted(emails))
                ]
            )
        
        return final_res



            

        