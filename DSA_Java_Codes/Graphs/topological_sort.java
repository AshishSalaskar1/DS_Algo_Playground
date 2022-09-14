package topological_sort;

import java.util.ArrayList;
import java.util.LinkedList;

class Graph{
	ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
	
	class Pair{
		int v;
		int distance;
		
		public Pair(int v, int distance) {
			this.v = v;
			this.distance = distance;
		}
		
		
	}
	
	Graph(int V){
		for(int i=0;i<=V;i++) {
			adj.add(new ArrayList<>());
		}
	}
	
	
	void add(int src,int dest) {
		adj.get(src).add(dest);
		adj.get(dest).add(src);
	}
	
	void addDir(int src,int dest) {
		adj.get(src).add(dest);
	}
	
	void print() {
		for (int i = 0; i < adj.size(); i++) {
			System.out.println(i+" : "+adj.get(i));
		}
	}
	
	//kahns algo for topological sort using BFS
	void topolical_sort_BFS() {
		ArrayList<Integer> res = new ArrayList<>();
		int V = adj.size();
		System.out.println(V);
		
		int[] indegree = new int[V];
		
		for(int i=1;i<V;i++ ) {
			for(int x : adj.get(i))
				indegree[x]++;
		}
		
		LinkedList<Integer> q =new LinkedList<>();
		int count = 0;
		
		for (int i = 1; i < indegree.length; i++) {
			if(indegree[i] == 0)
			{
				System.out.println("Added "+i);
				q.addLast(i);
			}
		}
		
		while(!q.isEmpty()) {
			int node = q.removeFirst();
			res.add(node);
			
			for(int x : adj.get(node)) {
				if(--indegree[x] == 0) {
					q.addLast(x);
				}
			}
			
			count++;
		}
		
		if(count != V-1) {
			System.out.println("Cycle Present");
			return;
		}
		
		System.out.println("Topological Sort");
		for(int x : res) {
			System.out.print(x+" ");
		}
	
		
	}
	
	
}

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g = new Graph(7);
		
		//TOPOLOGICAL sort works only only on directed + acyclic 
		
		g.addDir(1, 2);
		g.addDir(2, 3);
		g.addDir(2, 4);
		g.addDir(3, 6);
		g.addDir(6, 4);
		g.addDir(6, 7);
		
		g.print();

		g.topolical_sort_BFS();
	}

}

