
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

class Graph{
	class Vertex{
		HashMap<Integer,Integer> nbrs = new HashMap<>();
	}
	
	class Pair{
		int vname;
		String path;
		
		Pair(int n,String prevPath){
			vname = n;
			path = ""+prevPath+n;
		}
	}
	
	HashMap<Integer,Vertex> vtcs = new HashMap<>();
	
	void addEdge(int src,int dest,int wt) {
		if(!vtcs.containsKey(src)) {
			vtcs.put(src,new Vertex());
		}
		
		if(!vtcs.containsKey(dest)) {
			vtcs.put(dest,new Vertex());
		}
		
		vtcs.get(src).nbrs.put(dest,0);
		vtcs.get(dest).nbrs.put(src,0);
	}
	
	void print() {
		ArrayList<Integer> it = new ArrayList<>(vtcs.keySet());
		for(int key:it) {
			System.out.println(key+" : " +vtcs.get(key).nbrs);
		}
	}
	
	
	//Breadth First Traversal
	void BFT() {


		LinkedList<Pair> q = new LinkedList<>();
		boolean[] vis = new boolean[vtcs.size()+1];
		
		ArrayList<Integer> it = new ArrayList<>(vtcs.keySet());
		
		//check for all nodes in case of disconnected graphs
		for(int src: it) {
			
			if(vis[src]) {
				continue;
			}
			
			q.addLast(new Pair(src,""));
//			System.out.println("Inserted: "+src);
			
			while(!q.isEmpty()) {
				Pair rPair = q.removeFirst();
				
				int node = rPair.vname;
//				System.out.println("Removed: "+node);
				
				if(vis[node]) {
					continue;
				}
				
				vis[node] = true;
				System.out.println(node+ ":: "+rPair.path);
				
				ArrayList<Integer> keys = new ArrayList<>(vtcs.get(node).nbrs.keySet());
				for(int key:keys) {
					if(!vis[key]) {
//						System.out.println(key);
						q.addLast(new Pair(key,rPair.path));
					}
				}
				
			}
			//queue is empty
			
		}
		//all nodes checked as source
		
		
	}

	boolean isCyclic() {


		LinkedList<Pair> q = new LinkedList<>();
		boolean[] vis = new boolean[vtcs.size()+1];
		
		ArrayList<Integer> it = new ArrayList<>(vtcs.keySet());
		
		//check for all nodes in case of disconnected graphs
		for(int src: it) {
			
			if(vis[src]) {
				continue;
			}
			
			q.addLast(new Pair(src,""));
			
			while(!q.isEmpty()) {
				Pair rPair = q.removeFirst();
				
				int node = rPair.vname;
				
				if(vis[node]) {
					return true;
//					continue;
					
				}
				
				vis[node] = true;
				
				ArrayList<Integer> keys = new ArrayList<>(vtcs.get(node).nbrs.keySet());
				for(int key:keys) {
					if(!vis[key]) {
						q.addLast(new Pair(key,rPair.path));
					}
				}
				
			}
			
		}
		return false;	
	}

	int noOfComponents() {

		int components = 0;
		LinkedList<Pair> q = new LinkedList<>();
		boolean[] vis = new boolean[vtcs.size()+1];
		
		ArrayList<Integer> it = new ArrayList<>(vtcs.keySet());
		
		//check for all nodes in case of disconnected graphs
		for(int src: it) {
			
			if(vis[src]) {
				continue;
			}
			
			components++;
			
			q.addLast(new Pair(src,""));
			
			while(!q.isEmpty()) {
				Pair rPair = q.removeFirst();
				
				int node = rPair.vname;
				
				if(vis[node]) {
					continue;
					
				}
				
				vis[node] = true;
				
				ArrayList<Integer> keys = new ArrayList<>(vtcs.get(node).nbrs.keySet());
				for(int key:keys) {
					if(!vis[key]) {
						q.addLast(new Pair(key,rPair.path));
					}
				}
				
			}
			
		}
		return components;	
	}


	boolean isTree() {
		if ((this.noOfComponents() == 1) && !this.isCyclic()) {
			return true;
		}
		return false;
	}
}

public class GraphOps {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Graph g = new Graph();
		
		g.addEdge(1, 2, 0);
		g.addEdge(1, 4, 0);
		g.addEdge(2, 3, 0);
//		g.addEdge(3, 4, 0);
		g.addEdge(4, 5, 0);
//		g.addEdge(5, 6, 0);
		g.addEdge(5, 7, 0);
		g.addEdge(6, 7, 0);
		
		g.print();
		g.BFT();
		
		System.out.println(g.isCyclic());
		System.out.println(g.noOfComponents());
		System.out.println(g.isTree());

	}

}

