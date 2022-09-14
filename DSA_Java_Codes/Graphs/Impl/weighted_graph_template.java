package p1;

import java.util.*;
import java.lang.*;
import java.io.*;

class Main
 {
	static HashMap<Integer,Integer>[] adj;
	static int V;
	static boolean[] vis; 	
	static int[] parent;
	
	static void addEdge(int u,int v,int wt) {
		adj[u].put(v, wt);
		adj[v].put(u, wt);
	}
	
	static void addEdge(int u,int v) {
		adj[u].put(v, 0);
		adj[v].put(u, 0);
	}
 	
	static void print() {
		for(int i=1;i<=V;i++) {
			System.out.println(i+" : "+adj[i]);
		}
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
	public static void main (String[] args) throws Exception
	 {
	    
		V = 5;
	    adj = new HashMap[V+1];
	    
	    for(int i=0;i<=V;i++) {
	    	adj[i] = new HashMap<>();
	    }
	    
	    addEdge(1, 3, 3);
	    addEdge(1, 2, 2);
	    addEdge(3, 4, 5);
	    addEdge(3, 5, 4);
	    

	    

	
	    
	    
 	 }
}
