package p1;

import java.util.*;

class Node {
	        int destination;
	        int weight;

	        public Node(int destination, int weight) {
	            this.destination = destination;
	            this.weight = weight;
	        }
}
	


class Graph{
	ArrayList<Node>[] adj;
	int V;
	
	Graph(int V){
		this.V = V;
		adj = new ArrayList[V];
		
		for(int i=0;i<V;i++)
			adj[i] = new ArrayList<>();
	}
	
	void addEdge(int Src,int Dest,int w) {
		int src = Src-1;
		int dest = Dest-1;
		adj[src].add(new Node(dest,w));
		adj[dest].add(new Node(src,w));
	}
	
	int getSmallestIndex(int[] dist,boolean[] vis) {
		int minIndex = -1;
		
		for(int i=0;i<V;i++) {
			if(!vis[i] && (minIndex == -1 || dist[i]<dist[minIndex])) {
				minIndex = i;
			}
		}
		
		return minIndex;
	}

	
	void djikstras(int src) {
		int[] dist = new int[V];
		for(int i=0;i<V;i++)
			dist[i] = Integer.MAX_VALUE;
		
		boolean[] vis = new boolean[V];
		
		dist[src] = 0;
		
		for (int x = 0; x < V-1; x++) {
			int u = getSmallestIndex(dist, vis);
			vis[u] = true;
			
			for(Node node : adj[u]) {
				int v = node.destination;
				if(!vis[v]) {
					int wt = dist[u] + node.weight;
					if(wt < dist[v])
						dist[v] = wt;
				}
			}
			
		}
		
		for(int i=0;i<V;i++) {
			System.out.println(dist[i]);
		}
	}
	
}


class Solution {
	public static void main(String[] args) {
		Graph g = new Graph(4);
		g.addEdge(1,2 ,24 );
		g.addEdge(1, 4, 20);
		g.addEdge(3, 1, 3);
		g.addEdge(4, 3, 12);
		
		g.djikstras(0);
	}

}



