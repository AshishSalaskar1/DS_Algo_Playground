"""
Problem: Find All Possible Recipes from Given Supplies
Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/?envType=daily-question&envId=2025-03-21


Solution 1: BFS/DFS
Solution 2: Topo sort 
- Consider recipes are nodes 
- Indegree = how many ingredients are needed for that recipe
"""

from collections import deque
class SolutionDFS:
    @cache
    def can_make(self, recipe):
        ingr_needed = self.ri[recipe]
        for ingr in ingr_needed:
            if ingr in self.rset:
                if ingr in self.curtaken:
                    return False
                self.curtaken.add(recipe)
                poss =  self.can_make(ingr) 
            else:
                poss = ingr in self.sset
            
            if poss is False:
                return False

        return True

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        self.rset = set(recipes)
        self.sset = set(supplies)
        self.ri = {recipes[i]:ingredients[i] for i in range(len(recipes))}


        res = []

        for recipe, ing in self.ri.items():
            self.curtaken = set()
            if self.can_make(recipe):
                res.append(recipe)
        
        return res

        

class SolutionTopologicalSort:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {recipe:0 for recipe in recipes}
        dep = {recipe:set() for recipe in recipes}
        
        supplies = set(supplies)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingr in ingredients[i]:
                if ingr not in supplies:
                    indegree[recipe] += 1
                    dep[recipe].add(ingr)
        
        q = deque([recipe for recipe in recipes if indegree[recipe]==0])
        taken = []

        while len(q) != 0:
            prepared = q.popleft()
            taken.append(prepared)

            indegree.pop(prepared, None)
            dep.pop(prepared, None)

            for recipe in dep.keys():
                if prepared in dep[recipe]:
                    dep[recipe].remove(prepared)
                    indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    q.append(recipe)
    
        
        return list(set(taken))

        