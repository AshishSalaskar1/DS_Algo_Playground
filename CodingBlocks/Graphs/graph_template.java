package template;

import java.util.ArrayList;
import java.util.HashMap;

class Graph{
	class Vertex{
		HashMap<Integer,Integer> nbrs= new HashMap<>();
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
		
		if(v1 ==null || v2==null || v1.nbrs.containsKey(dest)) {
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
}

public class Graphs {
	public static void main(String[] args) {
		System.out.println("Hello");
		
		Graph g = new Graph();
		
		g.addEdge(1, 2, 0);
		g.addEdge(1, 3, 0);
		g.addEdge(3, 4, 0);
		g.addEdge(4, 5, 0);
		g.addEdge(2, 5, 0);
		
		g.display();
	}
}

