"""
SOLUTION:https://www.youtube.com/watch?v=dxVcMDI7vyI

"""

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arrive = sorted(arr)
        depart = sorted(dep)
        n = len(arr)
        
        # why i=1, assume one train has arrived and taking up one platform
        i,j = 1,0
        platforms, max_platforms = 1,1
        
        while i<n and j<n:
            # train arrive time < depart: means if this train arrived it will need +1 platform
            # because another train is stil standing and hasnt left
            if arrive[i]<=depart[j]:
                platforms += 1
                i += 1
            # a train leaves before this train arrives -> one platform reduced
            else:
                platforms -= 1
                j += 1
            
            max_platforms = max(max_platforms, platforms)
        
        return max_platforms