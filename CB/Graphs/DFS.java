
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Stack;

class Graph{
	class Vertex{
		HashMap<Integer,Integer> nbrs= new HashMap<>();
	}
	
	class Pair{
		int vname;
		String path;
		
		public Pair(int vname, String prevPath) {
			this.vname = vname;
			this.path = ""+prevPath+vname;
		}
		
		
	}
	
	HashMap<Integer,Vertex> vtcs = new HashMap<>();
	
	void addEdge(int src,int dest, int weight) {
		
		if(!vtcs.containsKey(src)) {
			vtcs.put(src, new Vertex());
		}
		
		if(!vtcs.containsKey(dest)) {
			vtcs.put(dest, new Vertex());
		}
		
		vtcs.get(src).nbrs.put(dest, weight);
		vtcs.get(dest).nbrs.put(src, weight);
	}
	
	boolean hasEdge(int src,int dest) {
		Vertex v1 = vtcs.get(src);
		Vertex v2 = vtcs.get(dest);
		
		if(v1 ==null || v2==null || !v1.nbrs.containsKey(dest)) {
			return false;
		}
		
		return true;
		
		
	}
	
	void display() {
		ArrayList<Integer> keys = new ArrayList<>(vtcs.keySet());
		for(int key:keys) {
			System.out.println(key+" : "+vtcs.get(key).nbrs);
		}
	}
	
	void DFS(int src){
		Stack<Integer> queue = new Stack<>();
		
		boolean[] vis = new boolean[vtcs.size()+1];
		
		queue.push(src);
		vis[src] = true;
		
		while(!queue.isEmpty()) {
			
			int node = queue.pop();
			vis[node] = true;

			System.out.print(node+"->");
			
			ArrayList<Integer> it = new ArrayList<>(vtcs.get(node).nbrs.keySet());
			for(int key: it) {
				if(!vis[key]) {
					queue.add(key);
				}
			}
			
		}
		
	}
	
	String DFS(int src,int dest) {
		
		Stack<Pair> q = new Stack<>();
		boolean[] vis = new boolean[vtcs.size()];
		
		vis[src] = true;
		q.push(new Pair(src," "));
		
		while(!q.isEmpty()) {
			Pair rPair = q.pop();
			int node = rPair.vname;
			vis[node] = true;

			System.out.println("Removed: "+node);
			
			ArrayList<Integer> it = new ArrayList<>(vtcs.get(node).nbrs.keySet());
			for(int key:it) {
				
				if(key == dest) {
					return ""+rPair.path+key;
				}
				
				if(!vis[key]) {
					System.out.println("\tInserted: "+key);
					q.push(new Pair(key,rPair.path));
				}
			}
			
		}
		
		return "";
	}
}


public class DFS {
	public static void main(String[] args) {
		System.out.println("Hello");
		
		Graph g = new Graph();
		
		g.addEdge(1, 2, 0);
		g.addEdge(1, 3, 0);
		g.addEdge(2, 4, 0);
		g.addEdge(2, 5, 0);
		g.addEdge(3, 4, 0);
		g.addEdge(4, 5, 0);
		
		
		g.display();
		
		g.DFS(1);
		System.out.println();
		System.out.println(g.DFS(1,5));
	
	}
}

