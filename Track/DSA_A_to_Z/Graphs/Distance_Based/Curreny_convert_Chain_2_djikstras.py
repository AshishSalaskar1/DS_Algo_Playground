"""
Problem: https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/description/

SOLUTION: 2 Dijkstras
1. On day 1 see the max you can earn -> dest currency doesnt matter [USE DIKSTRAS]
2. For each cur,profit pair from day 1 -> check if profit*max_cost[cur][init_currency] is bigger than res

TC:
1. Dijkstras with init_currency as src
2. Dijstras from each temp_curency as src and init_currency as dest

"""
from queue import PriorityQueue
from collections import defaultdict
class Solution:

    def djkistras(self, adj, src, init_amount = 1.0):
        max_amount = {node:0 for node in adj.keys()}
        max_amount[src] = init_amount
        pq = PriorityQueue()
        pq.put((init_amount,src))

        while not pq.empty():
            amt, node = pq.get()
            for nbr, cost in adj[node]:
                new_amount = amt*cost
                if new_amount > max_amount[nbr]:
                    max_amount[nbr] = new_amount
                    pq.put((new_amount, nbr))
        
        return max_amount
    

    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2) -> float:
        day1 = defaultdict(list)
        for i in range(len(pairs1)):
            src, dest, cost = pairs1[i][0], pairs1[i][1], rates1[i]
            day1[src].append((dest, cost))
            day1[dest].append((src, 1/cost))
        
        day2 = defaultdict(list)
        for i in range(len(pairs2)):
            src, dest, cost = pairs2[i][0], pairs2[i][1], rates2[i]
            day2[src].append((dest, cost))
            day2[dest].append((src, 1/cost))
        
        
        day1_res = self.djkistras(day1, initialCurrency)
        max_res = 1.0

        for currency, profit_till_now in day1_res.items():
            next_day_profit = self.djkistras(day2, currency)
            max_res = max(max_res, profit_till_now*next_day_profit.get(initialCurrency,0))
            
        
        return max_res
        