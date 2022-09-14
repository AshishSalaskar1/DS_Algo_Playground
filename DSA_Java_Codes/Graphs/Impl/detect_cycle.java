static boolean[] vis;
    
    static boolean dfs(int src,int parent,ArrayList<ArrayList<Integer>> list){
        vis[src] = true;
        
        for(int x : list.get(src) ){
            
            if(vis[x] && x!=parent)
                return true;
            
            else if(!vis[x])
                if( dfs(x,src,list))
                    return true;
        }
        
        return false;
    }
    
    static boolean isCyclic(ArrayList<ArrayList<Integer>> list, int V)
    {
        vis = new boolean[V];
        
        for(int i=0;i<V;i++){
            if(!vis[i])
                if(dfs(i,-1,list)) 
                    return true;
        }
        
        return false;
        
    }
