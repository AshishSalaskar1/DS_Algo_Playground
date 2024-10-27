package java1;

import java.io.*;
import java.util.*;


import java.math.*;

class Graph{
	ArrayList<Integer>[] adj;
	int V;
	
	
	Graph(int V){
		this.V =V;
		
		adj = new ArrayList[V+1];
		for(int i=1;i<=V;i++)
			adj[i] = new ArrayList<>();
	}
	
	void addEdge(int u,int v) {
		adj[u].add(v);
		adj[v].add(u);
	}
	
	void print() {
		for(int i=1;i<=V;i++)
			System.out.println(i+" : "+adj[i]);
	}
	
	void DFS(int src,boolean[] vis) {
		vis[src] = true;
		
		for(int x : adj[src])
			if(!vis[x])
				DFS(x, vis);
	}
	
	int no_of_components() {
		boolean[] vis = new boolean[V+1];
		
		int count = 0;
		
		for(int i=1;i<=V;i++)
			if(!vis[i]) {
				count++;
				DFS(i,vis);
			}
		
		return count;
	}
}

public class Sol2 {
	
	public static void main(String[] args) throws IOException{
		Graph g = new Graph(6);
		g.addEdge(1,2);
		g.addEdge(1,3);
		g.addEdge(3,2);
		g.addEdge(2,4);
		g.addEdge(4,5);
		g.addEdge(4,6);
		g.addEdge(5,6);
		
		g.print();
		
		System.out.println(g.no_of_components());
	}
		
		

}

/*
 * 
 * 
 * 
6 7
1 2
2 3
3 1
4 5
5 6
6 4
2 4
 * */

