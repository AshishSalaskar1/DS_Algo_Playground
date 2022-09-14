package java1;

import java.io.*;
import java.util.*;


// BACK EDGE : v -> node which is already visited & !its parent
class Pair{
	int a,b;
	Pair(int a,int b){
		this.a = a;
		this.b = b;
	}
	
	public String toString() {
		return a+","+b;
	}
}

class Graph{
	
	ArrayList<Pair> ans;
	
	int V;
	ArrayList<Integer>[] adj;
	
	Graph(int V){
		this.V = V;
		adj = new ArrayList[V+1];
		for(int i=1;i<=V;i++) {
			adj[i] = new ArrayList<Integer>();
		}
	}
	
	void addEdge(int u,int v) {
		this.adj[u].add(v);
		this.adj[v].add(u);
	}
	
	void printGraph() {
		for(int i=1;i<=V;i++) {
			System.out.println(i+" : "+adj[i]);
		}
	}
	
	
	ArrayList<Pair> bridge(int src) {
		int timer = 0;
		int[] in = new int[V+1];
		int[] low = new int[V+1];
		boolean[] vis = new boolean[V+1];
		
		bridgeUtil(src, -1, vis, low, in, timer);
		
		return this.ans;
		
		
	}
	
	private void bridgeUtil(int src,int parent,boolean[] vis,int[] low,int[] in,int timer) {
		timer++;
		in[src] = low[src] = timer;
		
		vis[src] = true;
		
		for(int child : adj[src]) {
			
			//parent edge
			if(child == parent) continue;
			
			//Back Edge - dont call DFS as visited
			if(vis[child]) {
				low[src] = Math.min(low[src], in[child]);
			}
			//Forward Edge
			else {
				bridgeUtil(child, src, vis, low, in, timer);
				
				//backtracking step 3->4 and comes back at 3
				//if lowest ancestor of child  > intime of src
				//which means child appeared after src and thus dependent
				if(low[child] > in[src])
				{
					System.out.println("Bridge at: "+src+" : "+child);
					this.ans.add(new Pair(src,child));
				}
				
				low[src] = Math.min(low[src], low[child]);
			}
		}
	}
}

public class Sol2 {
	
	public static void main(String[] args){
		
		System.out.println("Hello");
		Graph a = new Graph(5);
		a.addEdge(1, 3);
		a.addEdge(1, 2);
		a.addEdge(1, 4);
		a.addEdge(4, 5);
		a.addEdge(3, 2);
//		a.printGraph();
		a.dfs(1);
//		System.out.println(a.dfs(1));
		ArrayList<Pair> ans= a.bridge(1);
		for(Pair x: ans)
			System.out.println(x);
	
	}

}
