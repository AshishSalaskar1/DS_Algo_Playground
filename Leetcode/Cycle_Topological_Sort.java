class Solution {
    
    static int V;
    static List<List<Integer>> adj = new ArrayList<>(); 
    
    public boolean canFinish(int v, int[][] prerequisites) {
       V = v;
       for(int i=0;i<V;i++)
           adj.add(new ArrayList<Integer>());
        
        if(prerequisites.length == 0)
            return true;
        

       int[] indegree = new int[V];
       boolean[] vis = new boolean[V];
        Arrays.fill(vis,false);
        
       for(int[] x : prerequisites) {
            adj.get(x[0]).add(x[1]);
            indegree[x[1]]++;
       }
        System.out.println(adj);  
        
        ArrayList<Integer> res = new ArrayList<>();
        
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<V;i++)
            if(indegree[i] == 0)
                q.add(i);
        
        while( !q.isEmpty()){
            int node = q.poll();
            res.add(node);
            
            for(int x : adj.get(node)){
                indegree[x]--;
                
                if(indegree[x] == 0)
                    q.add(x);
            }  
        }
        
        return res.size() == V;
   
    }
}
