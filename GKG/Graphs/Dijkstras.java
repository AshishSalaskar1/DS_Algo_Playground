package dijkstras;

import java.util.Arrays;

class Graph{
	int[][] adj;
	
	Graph(int V){
		adj = new int[V][V];
	}
	
	void add(int src,int dest,int w) {
		adj[src][dest] = w;
		adj[dest][src] = w;
	}
	
	int findMinNode(boolean[] vis,int[] dist) {
		int minIndex = -1;
		
		for(int i=0;i<vis.length;i++) {
			if(!vis[i] && ( minIndex == -1 || dist[i] < dist[minIndex]) )
				minIndex = i;
		}
		
		return minIndex;
	}
	
	void dijkstras(int src) {
		int V = adj.length;
		int[] dist = new int[V];
		boolean[] vis = new boolean[V];
		
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[src] = 0;
		
		for(int j=0;j<V-1;j++) {
			int minNode = findMinNode(vis, dist);
			vis[minNode] = true;
			
			for(int i=0;i<V;i++) {
				if(adj[minNode][i]!=0 && !vis[i]) {
					int newDist = dist[minNode]+adj[minNode][i];
					
					if(newDist < dist[i])
						dist[i] = newDist;
				}
			}
		}
		
		System.out.println("The shortest paths from "+src+" are: ");
		for (int i = 0; i < dist.length; i++) {
			System.out.println(src+" -> "+i+" : "+dist[i]);
		}
		System.out.println();
		
	}
	
}

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g = new Graph(6);
		g.add(0,1,1);
		g.add(0,2,5);
		g.add(1,2,2);
		g.add(1,3,3);
		g.add(2,3,7);
		g.add(2,4,8);
		g.add(3,4,4);
		g.add(3,5,2);
		g.add(4,5,6);
		
		g.dijkstras(0);

	}

}

