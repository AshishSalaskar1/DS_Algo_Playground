package graphs;

import java.util.ArrayList;
import java.util.LinkedList;

class Graph{
	ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
	
	class Pair{
		int v;
		String path;
		
		Pair(int v,String prev){
			this.v = v;
			 this.path = ""+prev+v;
		}
	}
	
	Graph(int V){
		for(int i=0;i<=V;i++) {
			adj.add(new ArrayList<Integer>());
		}	
	}
	
	void add(int src,int dest) {
		adj.get(src).add(dest);
		adj.get(dest).add(src);
	}
	
	void addDirected(int src,int dest) {
		adj.get(src).add(dest);
	}
	
	void display() {
		for (int i = 1; i < adj.size(); i++) {
			System.out.println(i+" :"+adj.get(i));
		}
	}
	
	void BFS(int src) {
		System.out.println("BFS");
		boolean[] vis = new boolean[adj.size()];
		LinkedList<Integer> q = new LinkedList<>();
		q.addLast(src);
		
		while(!q.isEmpty()) {
			int node = q.removeFirst();
			System.out.println(node);
			vis[node] = true;
			
			for(int x: adj.get(node)) {
				if(!vis[x]) {
//					System.out.println("Added: "+x);
					vis[x] = true;
					q.addLast(x);
				}
			}
		}
	}
	
	String BFS(int src,int dest) {
		boolean[] vis = new boolean[adj.size()];
		LinkedList<Pair> q = new LinkedList<>();
		q.addLast(new Pair(src,""));
		
		while(!q.isEmpty()) {
			Pair Node = q.removeFirst();
			int node = Node.v;
//			System.out.print(node+" ");
			vis[node] = true;
			
			for(int x: adj.get(node)) {
				if(!vis[x]) {
					
					if(x == dest) {
//						System.out.println(dest);
						return Node.path+x;
					}
//					System.out.println("Added: "+x);
					vis[x] = true;
					q.addLast(new Pair(x,Node.path));
				}
			}
		}
		return "No Path";
	}
	
	void DFS(int src) {
		System.out.println("DFS");
		boolean[] vis = new boolean[adj.size()];
		LinkedList<Integer> q = new LinkedList<>();
		q.addFirst(src);
		
		while(!q.isEmpty()) {
			int node = q.removeFirst();
			System.out.println(node);
			vis[node] = true;
			
			for(int x: adj.get(node)) {
				if(!vis[x]) {
//					System.out.println("Added: "+x);
					vis[x] = true;
					q.addFirst(x);
				}
			}
		}
	}
	
	String DFS(int src,int dest) {
		boolean[] vis = new boolean[adj.size()];
		LinkedList<Pair> q = new LinkedList<>();
		q.addFirst(new Pair(src,""));
		
		while(!q.isEmpty()) {
			Pair Node = q.removeFirst();
			int node = Node.v;
			vis[node] = true;
			
			for(int x: adj.get(node)) {
				if(!vis[x]) {
					
					if(x == dest) {
						return Node.path+x;
					}
					vis[x] = true;
					q.addFirst(new Pair(x,Node.path));
				}
			}
		}
		return "No Path";
	}
	
	//works for directed -- similar to dfs
	private boolean isCyclicUtil(int node,boolean[] vis,boolean[] ancestor) {
		if(ancestor[node])
		{
			System.out.println("Cycle at "+node);
			return true;
		}
		
		ancestor[node] = true;
		
		for(int x : adj.get(node)) {
			if(!vis[x])
				if(isCyclicUtil(x, vis, ancestor))
					return true;
		}
		
		ancestor[node] = false;
		
		return false;
	}
	
	boolean isCyclic() {
		boolean[] vis = new boolean[adj.size()];
		boolean[] ancestor = new boolean[adj.size()];
		
		for(int i=0;i<adj.size();i++) {
			if(!vis[i])
				if(isCyclicUtil(i,vis,ancestor))
					return true;
		}
		
		return false;
	}
}

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g = new Graph(6);
		
		g.addDirected(0,1 );
		g.addDirected(1,2);
		g.addDirected(1,3);
		
//		g.add(2,3);
		
		g.display();
		
		System.out.println(g.isCyclic());
		
//		System.out.println(g.BFS(1,5));
//		System.out.println(g.DFS(1,5));
//		g.DFS(1);
//		g.BFS(1);
		

	}

}

