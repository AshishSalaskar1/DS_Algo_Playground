"""
PROBLEM: https://leetcode.com/problems/minimum-genetic-mutation

SOLUTION: Simple BFS
- Convert bank into hashset for O(1) lookup and deletion operations
- Instead of using a vis array, just pop the new_genes after its taken
"""

from collections import deque
class Solution:
    def minMutation(self, start_gene: str, end_gene: str, bank: List[str]) -> int:
        genes = ["A", "C", "G", "T"]
    
        bank = set(bank)
        q = deque([(start_gene, 0)])

        if end_gene not in bank:
            return -1

        while len(q) != 0:
            cur_gene, cur_len = q.popleft()

            for i,ch in enumerate(cur_gene):
                for gene in [x for x in genes if x!=cur_gene[i]]:
                    new_gene = cur_gene[:i] + gene + cur_gene[i+1:]
                    if new_gene in bank:
                        if new_gene == end_gene:
                            return cur_len + 1

                        bank.remove(new_gene)
                        q.append( (new_gene, cur_len+1) )
        
        return -1


        

        