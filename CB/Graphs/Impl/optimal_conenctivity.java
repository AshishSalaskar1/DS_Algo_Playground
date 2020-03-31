
import java.util.*;
import java.io.*;



class TestClass {

    static HashMap<Integer,Integer>[] adj;
	static int V;
	static boolean[] vis; 	
	static int[] parent;
	
	static void addEdge(int u,int v,int wt) {
		adj[u].put(v, wt);
		adj[v].put(u, wt);
	}
	
	
	
	static boolean checkPath(int u,int v,int lag) {
		
	    
	    
	    while ( u != v ) {
//	       	System.out.println(u+" : "+v);
	    	int U = u == -1 ? u : parent[u];
	    	int V = v == -1 ? v : parent[v];
	    	
	    	// System.out.println(u+"->"+U);
	    	// System.out.println(v+"->"+V);
	    	
	    	if(u!=-1 && U!=-1)
	    		if(lag < adj[u].get(U))
	    			return true;
	    
	    	if(v!=-1 && V!=-1)
	    		if(lag < adj[v].get(V))
	    			return true;
	    	
	    	u = U;
	    	v = V;
	    }
	    
	    return false;
	    
	    
	    
	    
	}
	
	static void dfs(int src,int par) {
		vis[src] = true;
		parent[src] = par;
		
		ArrayList<Integer> nbrs = new ArrayList<>(adj[src].keySet());
		
		for(int x : nbrs) 
			if(!vis[x])
				dfs(x,src);
		
	}

    @SuppressWarnings("unchecked")
    public static void main(String args[] ) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        V = n;

        adj = new HashMap[n+1];
        for(int i=1;i<=n;i++) adj[i] = new HashMap<>();

        for(int j=0;j<n-1;j++){
            String[] arr = br.readLine().trim().split(" ");
            addEdge(Integer.parseInt(arr[0]),Integer.parseInt(arr[1]),Integer.parseInt(arr[2]));
        }
        parent = new int[V+1];
		vis = new boolean[V+1];
		
		//populate weights
	    dfs(1,-1);
        
        int t = Integer.parseInt(br.readLine());

        while(t-- > 0){
            String[] arr = br.readLine().trim().split(" ");
            int u = Integer.parseInt(arr[0]);
            int v = Integer.parseInt(arr[1]);
            int w = Integer.parseInt(arr[2]);


            System.out.println(checkPath(u,v,w) ? "YES" : "NO");
        }


    }
}

